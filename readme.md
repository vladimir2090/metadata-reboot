# metadata-reboot

Tool for cleaning and correcting music file names and metadata with local AI.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Development Status](https://img.shields.io/badge/status-100%25%20complete-green.svg)

---

## 🚀 Release Status

**Progress:** 100%
metadata-reboot has reached its first stable release (v1.0.0).
Core features for editing music file metadata and filenames are complete and ready for production use.
Future updates will focus on additional optimizations, extended format support, and optional AI-powered metadata improvements.

---

## 📝 Description

**metadata-reboot** helps you quickly fix metadata and filenames for hundreds of music files with ease.

**Key features:**

* Cleans up metadata and filenames (requires title and artist present in source files)
* Uses local AI models (Llama) for smart analysis and correction
* Batch processing for large collections

---

## 🎯 Features

* **MP3 Metadata Parsing**: Reliable extraction via `mutagen`
* **AI Integration**: Uses local Llama models for processing
* **Batch Processing**: Edit large libraries in one go
* **YAML Configuration**: Custom processing options, model paths, tags, and renaming formats

---

## 📋 TODO

* [x] Core: AI metadata suggestions + updated file creation
* [x] `config.yaml` customization
* [x] Optimize & compress redundant metadata
* [x] Add `pyproject.toml` for modern project management

---

## 🔧 Current Functionality

### Metadata Extraction

* Extracts artist, album, title, date, genre, etc. – configurable tags
* Based on `mutagen.easyid3` for robust MP3 support

### AI Processing

* Integrated with `Llama.cpp`
* Customizable AI prompts for analysis
* Efficient chunk-wise library processing

### Configuration

* Configurable via YAML: model paths, options, tags
* Adjustable batch size for big libraries

### Error Handling

* Safe metadata/file error management
* Graceful model loading failures

---

## 🛠️ Installation & Usage

1. Clone the repo:

```bash
git clone https://github.com/vladimir2090/metadata-reboot.git
cd metadata-reboot
```

2.Install via setup.py:

```bash
pip install .
```

3.Download an AI model in GGUF format (recommended: Mistral-7B-Instruct-v0.3).
4.Configure your `config.yaml` (model paths, folders, tags, renaming, AI prompts).
5.Run in terminal:

```bash
meta-reboot
```

⚠️ Proper `config.yaml` configuration is required for successful operation!

---

## Dependencies

| Package                                                          | Version       | Purpose                              |
|------------------------------------------------------------------|---------------|--------------------------------------|
| [`mutagen`](https://pypi.org/project/mutagen/)                   | 1.47.0        | MP3/ID3 metadata reading & writing   |
| [`llama-cpp-python`](https://pypi.org/project/llama-cpp-python/) | 0.3.16        | Local Llama AI inference             |
| [`PyYAML`](https://pypi.org/project/PyYAML/)                     | 6.0.2         | YAML configuration parsing           |

---

## 🤝 Contributing

**Every contribution is important!**

* Bug reports
* Feature suggestions
* Code improvements
* Documentation
* Feedback and ideas

The project is developed by a beginner Python programmer, and community support is invaluable.

---

## 📄 License

metadata-reboot is released under the GNU GPL v3 license.
Feel free to use, modify, and distribute the code, provided your changes keep the same license.
See LICENSE for more details.

---

## 🧑💻 Contact & Links

**Author & Maintainer:**
[GitHub: vladimir2090](https://github.com/vladimir2090)

**Repository:**
[metadata-reboot GitHub repo](https://github.com/vladimir2090/metadata-reboot)

**For suggestions, feedback, or collaboration:**

* GitHub Issues at the repository page
* Direct message: [@vladimir2090 at GitHub](https://github.com/vladimir2090)

---

⭐ Star this project to follow updates and development progress!

---
