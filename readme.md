<h1 align="center">🎵 Metadata Reboot</h1>

<p align="center">
    <!-- Python Version -->
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/python-3.8+-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
    </a>
    <!-- License -->
    <a href="https://www.gnu.org/licenses/gpl-3.0">
        <img src="https://img.shields.io/badge/License-GPLv3-blue.svg" alt="License">
    </a>
    <!-- Release -->
    <a href="https://github.com/vladimir2090/metadata-reboot/releases">
        <img src="https://img.shields.io/github/v/release/vladimir2090/metadata-reboot?include_prereleases&color=orange&label=release" alt="Release">
    </a>
    <!-- Platform -->
    <img src="https://img.shields.io/badge/platform-linux%20%7C%20windows-lightgrey" alt="Platform">
</p>

**metadata-reboot** helps you quickly correct metadata and filenames for hundreds of music files using local AI models.

It performs batch processing of large music libraries through local packed AI models in `.gguf` format. Currently, only MP3 files are supported, but since this program is a Python script, you can easily implement your own improvements.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/vladimir2090/metadata-reboot.git
cd metadata-reboot
```

1. Install via setup.py

```bash
pip install .
```

1. Download an AI model in GGUF format (tested on [Mistral-7B-Instruct-v0.3](https://huggingface.co/MaziyarPanahi/Mistral-7B-Instruct-v0.3-GGUF)).

2. Configure your `config.yaml` (model paths, folders, tags, rename format, AI prompts).

3. Run in terminal:

```bash
meta-reboot
```

## Project Roadmap

- [ ] Add unit tests (in progress)
- [ ] Improve logging  (in progress)
- [x] Re-creating the project structure
- [ ] Integrate API key support and encryption for config security
- [ ] Add support for other music's formats
- [ ] Add command-line arguments similar to `yt-dlp`

---

### Recommended Models by Use Case

| Model                 | Параметры | VRAM (Q4_K_M) | URL                                                                      |
| --------------------- | --------- | ------------- | -------------------------------------------------------------------------|
| Mistral-7B-v0.3       | 7B        | ~5.5 GB       | <https://huggingface.co/MaziyarPanahi/Mistral-7B-Instruct-v0.3-GGUF>     |
| Mistral-Nemo-12       | 12B       | ~8.5 GB       | <https://huggingface.co/starble-dev/Mistral-Nemo-12B-Instruct-2407-GGUF> |
| Hermes-3-Llama-3.1-8B | 8B        | ~6.0 GB       | <https://huggingface.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF>         |
| Phigments-12B         | 12B       | ~8.0 GB       | <https://huggingface.co/mradermacher/Moonbright-12B-GGUF>                |
| Mixtral-8x7B-v0.1     | 8x7B      | ~26 GB        | <https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-GGUF>        |

⚠️ If your hardware doesn’t meet the minimum requirements, the model will still run, but token generation speed will be low.

---

## Dependencies

|                             Package                              | Version |         Purpose          |
|------------------------------------------------------------------|---------|--------------------------|
| [`mutagen`](https://pypi.org/project/mutagen/)                   | 1.45.0  | MP3/ID3 metadata reading |
| [`llama-cpp-python`](https://pypi.org/project/llama-cpp-python/) | 0.2.87  | Local Llama AI inference |
| [`PyYAML`](https://pypi.org/project/PyYAML/)                     | 5.4.0   | YAML configuration       |

---

## architecture

FFmpeg is used to completely remove the cover and then rebuild the container. When using mutagen, the cover is often not completely removed because it still takes up space.

YAML is used instead of JSON because YAML contains comments and is easier to read, which helps the user better understand and more easily edit the configuration file, which is the basis for configuring this program.

The code includes a metadata cleanup function, which essentially removes stopwords specified in config.yaml. This shortens the AI ​​input tokens, thereby speeding up the program. By default, N is used to replace stopwords.

The existing logging system includes the designation of message categories.

| Level   | Description                                                                                   | Code                                                                                                    |
| ------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| MSG     | Normal execution flow. Status updates and success confirmations.                              | [MSG] Model loaded<br>[MSG] Total files processed: 5                                                    |
| WARNING | Unexpected event, but execution continues. Often involves fallback values or skipping a step. | [SKIP] Corrupted file track.mp3: invalid header<br>[WARNING] Filename format error, using original name |
| ERROR   | Function failure. The operation for a specific file or batch completely failed.               | [ERROR] Model load failed: Out of memory<br>[ERROR]  Failed to apply changes for track.mp3              |

---

## License

metadata-reboot is released under the GNU GPL v3 license.  
You are free to use, modify, and distribute the code under the same license terms.  
See LICENSE for details.

## Contact & Links

**Author & Maintainer:**  
[GitHub: vladimir2090](https://github.com/vladimir2090)

**Repository:**  
[metadata-reboot GitHub repo](https://github.com/vladimir2090/metadata-reboot)

**For suggestions, feedback, or collaboration:**

- Open a GitHub Issue on the repository  
- Send a direct message: [@vladimir2090 on GitHub](https://github.com/vladimir2090)

---

⭐ Star this project to stay updated and support its development!
