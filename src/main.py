from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from llama_cpp import Llama
from pathlib import Path
import shutil
import multiprocessing
import re
import yaml
import atexit
import subprocess

class MusicProcessor:
    __slots__ = (
        "llm",
        "music_folder",
        "music_recode_folder",
        "tags",
        "system_prompt",
        "rename_format",
        "chunk_size",
        "stopwords",
        "remove_images",
    )

    def __init__(self, config_path: str = "config.yaml"):
        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.load(f, Loader=yaml.SafeLoader)

        self.music_folder = config["music_folder"]
        self.music_recode_folder = config["music_recode_folder"]
        self.tags = tuple(config["tags"])
        self.system_prompt = config["system_prompt"]
        self.rename_format = config["rename_format"]
        self.chunk_size = config["chunk_size"]
        self.stopwords = tuple(config["stopwords"])
        self.remove_images = config["remove_images"]

        try:
            self.llm = Llama(
                model_path=config["model_path"],
                n_ctx=4096,
                n_threads=multiprocessing.cpu_count() or 4
            )
            atexit.register(self._cleanup_llm)
            print("[MSG] Model loaded")
        except Exception as e:
            print(f"[ERROR] Model load failed: {e}")
            self.llm = None

        Path(self.music_recode_folder).mkdir(parents=True, exist_ok=True)

    def _cleanup_llm(self):
        if hasattr(self, "llm") and self.llm is not None:
            try:
                self.llm.close()
            except Exception:
                pass

    def clean_stopwords(self, text: str) -> str:
        if not text or text == "N":
            return text

        cleaned = text
        for word in self.stopwords:
            pattern = re.compile(rf"(?<!\w){re.escape(word)}(?!\w)", flags=re.IGNORECASE)
            cleaned = pattern.sub("", cleaned)

        cleaned = " ".join(cleaned.split())
        return cleaned if cleaned else "N"

    def extract_metadata(self, file_path):
        try:
            audio = EasyID3(file_path)
            metadata = {
                tag: audio[tag][0]
                if tag in audio and audio[tag] and audio[tag][0].strip()
                else "N"
                for tag in self.tags
            }

            cleaned_metadata = {k: self.clean_stopwords(v) for k, v in metadata.items()}
            filename = Path(file_path).name
            cleaned_filename = self.clean_stopwords(filename)

            return {
                "filename": filename,
                "cleaned_filename": cleaned_filename,
                "metadata": cleaned_metadata,
            }

        except Exception as e:
            print(f"[SKIP] Corrupted file {file_path}: {e}")
            return None

    def process_batch(self, batch):
        if not self.llm or not batch:
            return None

        files_data_yaml = yaml.dump(batch, allow_unicode=False, indent=2)
        prompt = f"{self.system_prompt}\n\n{files_data_yaml}"

        try:
            result = self.llm(
                f"[INST]\n{prompt}\n[/INST]",
                max_tokens=1024,
                temperature=0.8,
                top_p=0.9,
                top_k=50,
                min_p=0.05,
                repeat_penalty=1.1,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stream=False,
                stop=[],
                seed=0,
            )

            if isinstance(result, dict) and "choices" in result:
                ai_text = result["choices"][0]["text"].strip()
                raw = result["choices"][0]["text"]

                print("[MSG] FULL RESULT:", result)
                with open("debug_ai_response.txt", "w", encoding="utf-8") as f:
                    f.write(raw)

                return self.parse_ai_response(ai_text)

        except Exception as e:
            print(f"[ERROR] AI processing failed: {e}")
            return None

    def parse_ai_response(self, ai_text: str):
        try:
            return yaml.safe_load(ai_text)
        except yaml.YAMLError:
            match = re.search(r"\[.*\]", ai_text, re.DOTALL)
            if match:
                try:
                    return yaml.safe_load(match.group())
                except yaml.YAMLError:
                    pass
            return None

    def remove_album_art_with_ffmpeg(self, folder_path):
        folder = Path(folder_path)
        files = [f for f in folder.iterdir() if f.suffix.lower() == ".mp3"]
        removed_count = 0

        for file_path in files:
            temp_file = folder / f"_tmp_{file_path.name}"

            try:
                subprocess.run(
                    [
                        "ffmpeg", "-y",
                        "-i", str(file_path),
                        "-map_metadata", "0",
                        "-id3v2_version", "3",
                        "-c:a", "copy",
                        "-vn",
                        str(temp_file)
                    ],
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )

                temp_file.replace(file_path)
                print(f"[MSG] Cover removed: {file_path.name}")
                removed_count += 1

            except subprocess.CalledProcessError as e:
                print(f"[ERROR] Processing error {file_path.name}: {e.stderr.decode(errors='ignore')}")
                if temp_file.exists():
                    temp_file.unlink()

        print(f"\n[MSG] Total files processed: {len(files)}")
        print(f"[MSG] Covers removed: {removed_count}")

    def apply_changes(self, file_path, new_name, new_metadata):
        try:
            temp_path = Path(self.music_recode_folder) / Path(file_path).name
            shutil.copy2(file_path, temp_path)

            final_path = Path(self.music_recode_folder) / new_name
            audio = MP3(temp_path, ID3=EasyID3)

            for tag, value in new_metadata.items():
                if not value or value.strip() == "":
                    value = "N"
                audio[tag] = value

            if self.remove_images:
                self.remove_album_art_with_ffmpeg(final_path)

            audio.save()

            if temp_path != final_path:
                Path.replace(temp_path, final_path)

            print(f"[MSG] {Path(file_path).name} -> {final_path.name}")
            return True

        except Exception as e:
            print(f"[ERROR] Failed to apply changes for {file_path}: {e}")
            return False

    def run(self):
        mp3_files = list(Path(self.music_folder).glob("*.mp3"))
        if not mp3_files:
            print("[MSG] No MP3 files found.")
            return

        metadata_list = []
        for file_path in mp3_files:
            data = self.extract_metadata(str(file_path))
            if data:
                metadata_list.append(data)

        processed_count = 0
        for i in range(0, len(metadata_list), self.chunk_size):
            batch = metadata_list[i : i + self.chunk_size]
            ai_output = self.process_batch(batch)

            print("[MSG]", ai_output)
            if not ai_output:
                continue

            for old_data, new_data in zip(batch, ai_output):
                old_file = Path(self.music_folder) / old_data["filename"]

                try:
                    metadata = new_data.get("metadata", {})
                    required_fields = ["artist", "title", "album"]

                    safe_metadata = {}
                    for field in required_fields:
                        safe_metadata[field] = metadata.get(field, "N")

                    new_file_name = self.rename_format.format(**safe_metadata)
                    print("[MSG]", new_file_name)

                except (KeyError, ValueError) as e:
                    print(f"[WARNING] Filename format error: {e}, using original name")
                    new_file_name = old_data["filename"]

                applied = self.apply_changes(old_file, new_file_name, new_data["metadata"])

                if applied:
                    processed_count += 1
                    print(f"[MSG] Applied changes to {old_file}")


def main():
    MusicProcessor().run()


if __name__ == "__main__":
    main()