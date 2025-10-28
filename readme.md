# metadata-reboot

Tool for cleaning and correcting music file names and metadata with local AI.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)  
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)  
![Development Status](https://img.shields.io/badge/status-100%25%20complete-green.svg)

---

## 🚀 Release Status

Project **metadata-reboot** is now at version 1.2.0.  
Main changes since 1.1.0 include replacing the JSON configuration file with YAML for greater flexibility, adding a modern `pyproject.toml`, test coverage, and a rewritten README for clarity and usability.

---

## 📝 Description

**metadata-reboot** helps you quickly correct metadata and filenames for hundreds of music files using local AI models.

It performs batch processing of large music libraries through local packed AI models in `.gguf` format. Currently, only MP3 files are supported, but since this program is a Python script, you can easily implement your own improvements. The Pull Requests section is always open for your contributions!

---

## 🔧 Current Functionality

### Metadata Extraction

* Extracts artist, album, title, date, genre, and other tags — all configurable
* Built on `mutagen.easyid3` for stable and reliable MP3 support

### AI Processing

* Integrated with `Llama.cpp` for local `.gguf` model inference
* Nearly full customization via the config file (except low-level parameters of the AI model)
* Efficient chunk-wise (batch) library processing

### Configuration

* YAML-based configuration: model paths, parameters, tags, and renaming formats
* Adjustable batch size for large libraries (recommended 5–15 to avoid context overflow; depends on model size)

### Error Handling

* Safe file handling — automatically creates file backups (a toggleable option is planned)
* Robust and lightweight error management — problematic files in a batch are skipped gracefully

---

## 📋 Project Roadmap

[] Add unit tests (in progress)  
[] Improve logging  
[] Integrate API key support and encryption for config security  
[] Add support for popular formats beyond MP3  
[] Add command-line arguments similar to `yt-dlp`  
[] Implement multithreading and parallel script execution

---

## 🛠️ Installation & Usage

1. Clone the repository:

```bash
git clone https://github.com/vladimir2090/metadata-reboot.git
cd metadata-reboot
```

2. Install via setup.py

```bash
pip install .
```

3. Download an AI model in GGUF format (tested on Mistral-7B-Instruct-v0.3).

4. Configure your `config.yaml` (model paths, folders, tags, rename format, AI prompts).

5. Run in terminal:

```bash
meta-reboot
```

⚠️ A properly configured `config.yaml` file is required for successful execution!

### ⚙️ Recommended Models by Use Case

| Model | Parameters | Practical Context (tokens) | Recommended Batch | Typical Task | Quality (out of 10) | Min. Requirements | Recommended Requirements |
|--------|------------|---------------------------|------------------|---------------|----------------------|------------------|--------------------------|
| **Qwen2.5 0.5B** | 0.5B | 300–500 | 1–2 | Basic tag normalization | 3.5 | 2GB VRAM / CPU | 4GB VRAM |
| **Gemma 2B** | 2B | 400–600 | 1–3 | Basic normalization, simple corrections | 4 | 4GB VRAM / CPU | 6GB VRAM |
| **Phi-3 Mini 3.8B** | 3.8B | 500–800 | 2–5 | Tag normalization, light grammar fixes | 5 | 8GB VRAM | 12GB VRAM |
| **Mistral 7B** | 7B | 600–1000 | 5–10 | Grammar correction, template alignment | 6 | 8GB VRAM (Q4) | 16GB VRAM |
| **Qwen2.5 7B** | 7B | 800–1200 | 5–10 | Light to medium language corrections | 6.5 | 8GB VRAM (Q4) | 16GB VRAM |
| **Llama 3.1 8B** | 8B | 800–1500 | 5–15 | Medium editing, data structuring | 7 | 10GB VRAM (Q4) | 20GB VRAM |
| **Mistral Nemo 12B** | 12B | 1000–2000 | 8–20 | Data completion, medium corrections | 7 | 16GB VRAM (Q4) | 24GB VRAM |
| **Qwen2.5 14B** | 14B | 1200–2000 | 10–25 | Context-based data recovery | 7.5 | 16GB VRAM (Q4) | 24GB VRAM |
| **Phi-3 Medium 14B** | 14B | 1000–1800 | 10–20 | Medium/complex corrections, analysis | 7.5 | 16GB VRAM (Q4) | 24GB VRAM |
| **Qwen2.5 32B** | 32B | 2000–4000 | 20–50 | Complex data reconstruction, deep analysis | 8.5 | 24GB VRAM (Q4) | 48GB VRAM |
| **Llama 3.1 70B** | 70B | 3000–8000 | 30–80 | Large-scale dataset analysis | 9 | 48GB VRAM (Q4) / 2×3090 | 80GB VRAM |
| **Qwen2.5 72B** | 72B | 4000–8000 | 40–100 | Context memory-based data reconstruction | 9 | 48GB VRAM (Q4) / 2×3090 | 80GB VRAM |
| **Llama 4 Scout (109B, 17B active)** | 109B (17B active) | 8000–15000 | 80–200 | Processing of extremely large libraries | 9.5 | 48GB VRAM (Q4) / A6000 | 80GB VRAM |

⚠️ If your hardware doesn’t meet the minimum requirements, the model will still run, but token generation speed will be low.

---

## Dependencies

| Package | Version | Purpose |
|----------|----------|----------|
| [`mutagen`](https://pypi.org/project/mutagen/) | 1.47.0 | MP3/ID3 metadata reading & writing |
| [`llama-cpp-python`](https://pypi.org/project/llama-cpp-python/) | 0.3.16 | Local Llama AI inference |
| [`PyYAML`](https://pypi.org/project/PyYAML/) | 6.0.2 | YAML configuration parsing |

---

## 🤝 Contributing

**Every contribution matters!**

* Bug reports  
* Feature suggestions  
* Code improvements  
* Documentation updates  
* Feedback and ideas  

The project is developed by a beginner Python programmer; community support is deeply appreciated.

---

## 📄 License

metadata-reboot is released under the GNU GPL v3 license.  
You are free to use, modify, and distribute the code under the same license terms.  
See LICENSE for details.

---

## 🧑💻 Contact & Links

**Author & Maintainer:**  
[GitHub: vladimir2090](https://github.com/vladimir2090)

**Repository:**  
[metadata-reboot GitHub repo](https://github.com/vladimir2090/metadata-reboot)

**For suggestions, feedback, or collaboration:**

* Open a GitHub Issue on the repository  
* Send a direct message: [@vladimir2090 on GitHub](https://github.com/vladimir2090)

---

⭐ Star this project to stay updated and support its development!
