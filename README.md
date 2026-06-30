<div align="center">

![AI Email Analyzer Banner](assets/email_analyzer_banner.svg)

# 📧 AI Email Analyzer
### 🤖 Summarize, Score Risk & Draft Replies using Local AI (Ollama + Streamlit)

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-000000?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com/)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](#-license)
[![Privacy](https://img.shields.io/badge/Privacy-First-2563EB?style=for-the-badge)](#-features)

⭐ **If you like this project, don't forget to Star the Repository!** ⭐

[Features](#-features) • [Demo](#-application-preview) • [Installation](#%EF%B8%8F-installation) • [How It Works](#-how-it-works) • [Author](#%E2%80%8D-author)

</div>

---

## 📌 Project Overview

**AI Email Analyzer** is an AI-powered web application developed using **Python, Streamlit, and Ollama**.

The application allows users to upload `.eml` files or paste raw email text, automatically extract headers, body, links, and attachments, and use a **Local Large Language Model (LLM)** to understand, score, and respond to the email.

Unlike cloud-based AI tools, this project runs **completely offline** using Ollama — ensuring full privacy while providing intelligent, instant email analysis. Ideal for handling sensitive correspondence securely.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📨 Multiple Input Methods | Upload `.eml` files or paste raw email text |
| 📖 Header & Body Extraction | Automatically parses From, To, Subject, Date, body, links and attachments |
| 📊 Email Statistics | Shows word count, link count and attachment count |
| 🤖 AI Smart Summary | Generates intent, tone, urgency level and action items |
| 🚩 Phishing & Spam Risk Check | Rule-based heuristic scan + AI second opinion, scored 0–100 |
| ✍️ Reply Drafting | Generates a ready-to-send reply in your chosen tone |
| 🔑 Keyword Extraction | Finds important keywords from the email body |
| 🧵 Thread Summarization | Summarizes a full back-and-forth conversation into one overview |
| 📥 Download Report | Download the AI-generated analysis or reply draft |
| 🌙 Modern UI | Beautiful dark-themed Streamlit interface |
| 🔒 Local AI | Runs completely offline using Ollama |

---

## 🖥 Application Preview

<div align="center">

| Email Summary | Phishing Risk Check | Reply Drafting |
|:---:|:---:|:---:|
| ![Summary screenshot](screenshots/summary.png) | ![Risk screenshot](screenshots/risk_check.png) | ![Reply screenshot](screenshots/reply_draft.png) |

</div>

> 📌 *Drop your own screenshots into `screenshots/` using the filenames above and they'll render automatically.*

---

## 🚀 How It Works

```
Upload .eml / Paste Email Text
            │
            ▼
Parse Headers, Body, Links, Attachments
            │
            ▼
Run Heuristic Risk Scan
            │
            ▼
Send Prompt to Ollama
            │
            ▼
AI Analysis
            │
            ▼
Display Results
            │
            ▼
Draft Reply / Summarize Thread
```

---

## 🧠 AI Capabilities

The AI model can perform:

- 📄 Email Summarization
- 🎯 Intent & Tone Detection
- ⏰ Urgency Level Assessment
- ✅ Action Item Extraction
- 📅 Deadline Detection
- 🛡 Phishing / Spam Risk Assessment
- 🔑 Keyword Generation
- ✍️ Reply Drafting (multiple tones)
- 🧵 Thread Summarization

---

## 📂 Project Structure

```
AI-Email-Analyzer/
│
├── assets/
├── screenshots/
│   ├── homepage.png
│   ├── upload.png
│   ├── risk_check.png
│   ├── summary.png
│   └── reply_draft.png
│
├── analyzer.py
├── app.py
├── email_reader.py
├── risk_scoring.py
├── prompt.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/EmaanAftab/AI-Email-Analyzer.git
cd AI-Email-Analyzer
```

### 2️⃣ Create a Virtual Environment

**Windows**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

### 🦙 Install Ollama

This project uses Ollama to run a local Large Language Model (LLM).

👉 Download from **https://ollama.com/download**

Verify installation:
```bash
ollama --version
```

### 📥 Download an AI Model

```bash
ollama pull llama3.2:1b
```

Other supported models: `llama3.2`, `llama3.1`, `mistral`, `gemma`, `phi3`

### ▶️ Start Ollama

```bash
ollama serve
```

If everything is working correctly, the app sidebar will show **🟢 Ollama Online**.

### 🚀 Run the Application

```bash
python -m streamlit run app.py
```

Opens automatically at **http://localhost:8501**

---

## 📋 Supported Input Types

| Input Type | Supported |
|---|---|
| `.eml` File Upload | ✅ |
| Pasted Raw Email Text | ✅ |
| `.msg` (Outlook) | ❌ (export as `.eml` first) |

---

## 💡 Example Workflow

**Step 1** — Upload an `.eml` file or paste email text.
↓
**Step 2** — The app extracts headers, body, links and attachments automatically.
↓
**Step 3** — View the instant phishing/spam risk score and flagged reasons.
↓
**Step 4** — Click **🚀 Analyze Email**.
↓
**Step 5** — Receive: Summary · Intent · Tone · Urgency Level · Action Items · Deadlines
↓
**Step 6** — Click **✍️ Generate Reply Draft**.
↓
**Step 7** — Paste multiple thread messages to get a combined thread summary.
↓
**Step 8** — Download the AI-generated analysis or reply draft.

---

## 💻 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend Programming |
| Streamlit | Web Interface |
| Ollama | Local AI Model |
| Requests | API Communication |
| `email` (stdlib) | `.eml` Parsing |
| `re` (stdlib) | Heuristic Risk Scoring |
| Markdown | Report Formatting |

---

## 📦 Python Modules

```
streamlit
requests
```

All dependencies are listed in `requirements.txt`.

---

## 🔥 Key Highlights

✅ Runs completely offline
✅ No cloud API required
✅ Privacy-friendly
✅ Modern user interface
✅ Supports `.eml` files and pasted text
✅ Local AI using Ollama
✅ Instant phishing/spam risk scoring
✅ AI-generated reply drafting
✅ Multi-message thread summarization

---

## 🔮 Future Improvements

- 🌍 Multi-language email analysis
- 📎 Attachment content scanning (PDF/DOCX inside emails)
- 🖼 OCR support for image-based emails
- 📊 AI-powered sender/risk trend dashboard
- 📥 Direct inbox connection (IMAP/Gmail API)
- 💾 Persistent chat/thread history
- ☁ Cloud deployment (Streamlit Cloud / Hugging Face / Render)
- 👥 User authentication and profiles
- 📱 Mobile-friendly responsive interface
- 🔍 Bulk email batch analysis

---

## ❓ FAQ

<details>
<summary><b>Does this send my emails anywhere?</b></summary>
<br>
No. Every AI call goes to your local Ollama instance at <code>localhost:11434</code>. Nothing is uploaded to any external server.
</details>

<details>
<summary><b>Can it read .msg (Outlook) files?</b></summary>
<br>
Not directly — Outlook's binary <code>.msg</code> format isn't supported by Python's standard library. Export the email as <code>.eml</code> first (most clients support "Download message" or "Show original").
</details>

<details>
<summary><b>How accurate is the phishing detector?</b></summary>
<br>
The heuristic score is a helpful first-pass signal, not a guarantee. Always verify suspicious senders through an official channel rather than relying solely on this tool.
</details>

---

## 🤝 Contributing

Contributions are always welcome!

1. Fork this repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

## 🐞 Report Issues

Found a bug or have a suggestion? Please open an issue on GitHub — your feedback helps improve this project.

---

## 📄 License

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute this project for educational and personal purposes. See the LICENSE file for more details.

---

## 👩‍💻 Author

**Emaan Aftab**
BS Artificial Intelligence Student
Pak-Austria Fachhochschule Institute of Applied Sciences and Technology (PAF-IAST)
📍 Abbottabad, Pakistan

**Connect with me**
🐙 GitHub — https://github.com/EmaanAftab
💼 LinkedIn — https://www.linkedin.com/in/emaan-aftab-77bb88302/

---

## 💖 Support This Project

If you found this project helpful, please consider giving it a ⭐ on GitHub. It motivates me to build more AI and Machine Learning projects.

## 🙏 Acknowledgements

Special thanks to the open-source community and the developers of **Python, Streamlit, and Ollama**. Their amazing tools made this project possible.

<div align="center">

⭐ **If you like this project, don't forget to Star the Repository!** ⭐

Made with ❤️ using Python, Streamlit and Ollama.

© 2026 Emaan Aftab. All Rights Reserved.

</div>
