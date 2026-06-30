# 📧 AI Email Analyzer

AI Email Analyzer is a privacy-first Streamlit app that summarizes your emails, flags phishing/spam risk, and drafts replies — all running locally through [Ollama](https://ollama.com), so your data never leaves your machine.

![AI Email Analyzer Banner](assets/email_analyzer_banner.svg)

---

## ✨ Features

- **📝 AI Summary** — intent, tone, urgency level, action items, and mentioned deadlines, ending in a clear "reply now / later / archive" verdict.
- **🚩 Phishing & Spam Risk Check** — an instant rule-based heuristic scan (urgency language, sensitive-info requests, suspicious link domains, sender/reply-to mismatches, generic greetings) scored 0–100, plus an optional AI second opinion.
- **✍️ Reply Drafting** — generate a ready-to-send reply in your choice of tone (professional, friendly, apologetic, firm, brief), with optional custom instructions like "decline politely" or "ask for a deadline extension."
- **🔑 Keyword Extraction** — pulls out the most relevant terms from the email body.
- **🧵 Thread Summary** — paste multiple messages from a back-and-forth conversation and get a single combined summary of what happened and what's next.
- **📎 Attachment & Link Listing** — see attachments (name/size) and extracted links at a glance.
- **🔒 100% Local** — no API keys, no cloud calls, nothing leaves your machine.

---

## 🚀 Getting Started

### 1. Clone or download this repo

```bash
cd email-analyzer
```

### 2. Create a virtual environment (recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Ollama

```bash
ollama serve
```

### 5. Pull a model (only needed once)

```bash
ollama pull llama3.2:1b
```

### 6. Run the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

---

## 📁 Project Structure

```
email-analyzer/
├── app.py              # Streamlit UI
├── analyzer.py         # Ollama connection, retries, caching
├── email_reader.py     # .eml / pasted-text parsing
├── risk_scoring.py      # Phishing/spam heuristic scorer
├── prompt.py            # Prompt templates
├── requirements.txt
├── README.md
├── .gitignore
├── assets/              # banner / logo images
└── screenshots/         # app screenshots
```

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io) — UI framework
- [Ollama](https://ollama.com) — local LLM runtime
- Python's built-in `email` module — `.eml` parsing
- `requests` — Ollama API communication

---

## ⚠️ Notes

- `.msg` (Outlook binary format) isn't supported by the standard library — export as `.eml` first if your client allows it.
- The phishing risk score is a heuristic aid, not a guarantee. Always verify suspicious senders through an official channel rather than relying solely on this tool.
- Larger emails are automatically truncated before being sent to the model to avoid context overflow.

---

## 📄 License

This project is open for personal and educational use. Feel free to fork and adapt it.