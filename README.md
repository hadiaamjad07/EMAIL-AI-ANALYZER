<div align="center">

![AI Email Analyzer Banner](assets/email_analyzer_banner.svg)

# 📧 AI Email Analyzer

### Summarize. Detect Risk. Draft Replies. — 100% Local, 100% Private.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-000000?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com/)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](#-license)
[![Privacy](https://img.shields.io/badge/Privacy-First-2563EB?style=for-the-badge)](#-features)

**AI Email Analyzer** reads your emails and gives you instant, actionable insight — summarized intent, phishing/spam risk scoring, drafted replies, and thread summaries — without ever sending a single byte to the cloud.

[Features](#-features) • [Demo](#-demo) • [Quick Start](#-quick-start) • [Project Structure](#-project-structure) • [FAQ](#-faq)

</div>

---

## 🎬 Demo

<div align="center">

| Single Email Analysis | Phishing Risk Detection | Reply Drafting |
|:---:|:---:|:---:|
| ![Summary screenshot](screenshots/summary.png) | ![Risk screenshot](screenshots/risk_check.png) | ![Reply screenshot](screenshots/reply_draft.png) |

</div>

> 📌 *Drop your own screenshots into the `screenshots/` folder using these exact filenames and they'll render automatically above.*

---

## ✨ Features

<table>
<tr>
<td width="50%" valign="top">

### 📝 Smart Summarization
Get the intent, tone, and urgency of any email at a glance, plus extracted action items and deadlines — ending in a clear **reply now / later / archive** verdict.

### 🚩 Phishing & Spam Detection
An instant rule-based scanner flags urgency language, sensitive-info requests, suspicious domains, and sender/reply-to mismatches — scored 0–100 — backed up by an optional AI second opinion.

### ✍️ Reply Drafting
Generate a ready-to-send reply in **Professional, Friendly, Apologetic, Firm, or Brief** tone, with optional custom instructions like *"decline politely"* or *"ask for an extension."*

</td>
<td width="50%" valign="top">

### 🔑 Keyword Extraction
Instantly surface the most relevant terms from any email body.

### 🧵 Thread Summarization
Paste in a full back-and-forth conversation and get one summary covering what happened, who wants what, and what's next.

### 🔒 Fully Local & Private
Powered entirely by [Ollama](https://ollama.com) running on your own machine. No API keys. No cloud calls. Nothing leaves your computer — ideal for sensitive correspondence.

</td>
</tr>
</table>

---

## 🚀 Quick Start

```bash
# 1. Move into the project folder
cd email-analyzer

# 2. (Recommended) create a virtual environment
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start Ollama (separate terminal, keep it running)
ollama serve

# 5. Pull a model (only needed once)
ollama pull llama3.2:1b

# 6. Launch the app
streamlit run app.py
```

The app opens automatically at **http://localhost:8501** 🎉

---

## 🖥️ How It Works

```
┌─────────────────┐     ┌──────────────────┐     ┌────────────────────┐
│  Upload .eml /   │ ──▶ │  Parse headers,   │ ──▶ │  Heuristic risk     │
│  paste email     │     │  body, links,     │     │  scan (instant)     │
│  text            │     │  attachments      │     │                     │
└─────────────────┘     └──────────────────┘     └─────────┬──────────┘
                                                              │
                          ┌───────────────────────────────────┘
                          ▼
                ┌──────────────────────┐
                │   Local Ollama LLM    │ ──▶  Summary · Reply Draft
                │   (your machine)      │       Keywords · Thread Recap
                └──────────────────────┘
```

---

## 📁 Project Structure

```
email-analyzer/
├── app.py              # Streamlit UI
├── analyzer.py          # Ollama connection, retries, caching
├── email_reader.py      # .eml / pasted-text parsing
├── risk_scoring.py       # Phishing/spam heuristic scorer
├── prompt.py             # Prompt templates
├── requirements.txt
├── README.md
├── .gitignore
├── assets/               # banner / logo images
└── screenshots/          # app screenshots
```

---

## 🛠️ Built With

| Tool | Purpose |
|---|---|
| [Streamlit](https://streamlit.io) | Web UI framework |
| [Ollama](https://ollama.com) | Local LLM runtime |
| Python `email` module | `.eml` parsing |
| `requests` | Ollama API communication |

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

<details>
<summary><b>What model should I use?</b></summary>
<br>
<code>llama3.2:1b</code> is fast and lightweight for testing. For better quality summaries/replies, try a larger model like <code>llama3.1:8b</code> if your hardware supports it.
</details>

---

## 📄 License

This project is open for personal and educational use under the MIT License. Feel free to fork, modify, and build on it.

<div align="center">

Made with ☕ and a healthy distrust of phishing emails.

</div>
