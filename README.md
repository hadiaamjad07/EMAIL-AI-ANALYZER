📧 AI Email Analyzer
🤖 Analyze, Score & Reply to Emails using Local AI (Ollama + Streamlit)



📌 Project Overview
AI Email Analyzer is an AI-powered web application developed using Python, Streamlit, and Ollama.

The application allows users to upload .eml files or paste raw email text, automatically extract headers, body, links and attachments, and use a Local Large Language Model (LLM) to understand, score, and respond to the email.

Unlike cloud-based AI tools, this project runs completely offline using Ollama, ensuring privacy while providing intelligent email analysis — ideal for handling sensitive correspondence securely.

✨ Features
Feature	Description
📨 Multiple Input Methods	Upload .eml files or paste raw email text
📖 Header & Body Extraction	Automatically parses From, To, Subject, Date, body, links and attachments
📊 Email Statistics	Shows word count, link count and attachment count
🤖 AI Smart Summary	Generates intent, tone, urgency level and action items
🚩 Phishing & Spam Risk Check	Rule-based heuristic scan + AI second opinion, scored 0-100
✍️ Reply Drafting	Generates a ready-to-send reply in your chosen tone
🔑 Keyword Extraction	Finds important keywords from the email body
🧵 Thread Summarization	Summarizes a full back-and-forth conversation into one overview
📥 Download Report	Download the AI-generated analysis or reply draft
🌙 Modern UI	Beautiful dark-themed Streamlit interface
🔒 Local AI	Runs completely offline using Ollama
🖥 Application Preview
🏠 Home Page

📂 Upload / Paste Email

🚩 Phishing Risk Check

🤖 AI Smart Summary

✍️ Reply Draft

🧵 Thread Summary

🚀 How It Works
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
🧠 AI Capabilities
The AI model can perform:

📄 Email Summarization
🎯 Intent & Tone Detection
⏰ Urgency Level Assessment
✅ Action Item Extraction
📅 Deadline Detection
🛡 Phishing / Spam Risk Assessment
🔑 Keyword Generation
✍️ Reply Drafting (multiple tones)
🧵 Thread Summarization
📂 Project Structure
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
⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/EmaanAftab/AI-Email-Analyzer.git
Move into the project folder:

cd AI-Email-Analyzer
2️⃣ Create a Virtual Environment
Windows
python -m venv .venv
Activate it:

.venv\Scripts\activate
Linux / macOS
python3 -m venv .venv

source .venv/bin/activate
3️⃣ Install Required Packages
pip install -r requirements.txt
🦙 Install Ollama
This project uses Ollama to run a local Large Language Model (LLM).

Download Ollama from:

👉 https://ollama.com/download

After installation, verify it is installed:

ollama --version
📥 Download an AI Model
Download a lightweight model:

ollama pull llama3.2:1b
You can also use other supported models such as:

llama3.2
llama3.1
mistral
gemma
phi3
▶️ Start Ollama
Before running the application, start the Ollama server:

ollama serve
If everything is working correctly, the application sidebar will display:

🟢 Ollama Online
🚀 Run the Application
Run the Streamlit app:

python -m streamlit run app.py
The application will open automatically in your browser.

Default URL:

http://localhost:8501
📋 Supported Input Types
Input Type	Supported
.eml File Upload	✅
Pasted Raw Email Text	✅
.msg (Outlook)	❌ (export as .eml first)
💡 Example Workflow
Step 1
Upload an .eml file or paste email text.

↓

Step 2
The application extracts headers, body, links and attachments automatically.

↓

Step 3
View the instant phishing/spam risk score and flagged reasons.

↓

Step 4
Click:

🚀 Analyze Email
↓

Step 5
Receive:

📄 Summary
🎯 Intent
😊 Tone
⏰ Urgency Level
✅ Action Items
📅 Deadlines
↓

Step 6
Click:

✍️ Generate Reply Draft
↓

Step 7
Paste multiple thread messages to get a combined thread summary.

↓

Step 8
Download the AI-generated analysis or reply draft.

💻 Technologies Used
Technology	Purpose
Python	Backend Programming
Streamlit	Web Interface
Ollama	Local AI Model
Requests	API Communication
email (stdlib)	.eml Parsing
re (stdlib)	Heuristic Risk Scoring
Markdown	Report Formatting
📦 Python Modules
This project uses:

streamlit
requests
All dependencies are listed in requirements.txt.

🔥 Key Highlights
✅ Runs completely offline

✅ No cloud API required

✅ Privacy-friendly

✅ Modern user interface

✅ Supports .eml files and pasted text

✅ Local AI using Ollama

✅ Instant phishing/spam risk scoring

✅ AI-generated reply drafting

✅ Multi-message thread summarization

🔮 Future Improvements
The following features can be added in future versions of the project:

🌍 Multi-language email analysis
📎 Attachment content scanning (PDF/DOCX inside emails)
🖼 OCR support for image-based emails
📊 AI-powered sender/risk trend dashboard
📥 Direct inbox connection (IMAP/Gmail API)
💾 Persistent chat/thread history
☁ Cloud deployment (Streamlit Cloud / Hugging Face / Render)
👥 User authentication and profiles
📱 Mobile-friendly responsive interface
🔍 Bulk email batch analysis
🤝 Contributing
Contributions are always welcome!

If you'd like to improve this project:

Fork this repository.
Create a new feature branch.
Commit your changes.
Push your branch.
Open a Pull Request.
🐞 Report Issues
Found a bug or have a suggestion?

Please open an issue on GitHub.

Your feedback helps improve this project.

📄 License
This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and personal purposes.

See the LICENSE file for more details.

👩‍💻 Author
Emaan Aftab
BS Artificial Intelligence Student

Pak-Austria Fachhochschule Institute of Applied Sciences and Technology (PAF-IAST)

📍 Abbottabad, Pakistan

Connect with me
🐙 GitHub

https://github.com/EmaanAftab

💼 LinkedIn

https://www.linkedin.com/in/emaan-aftab-77bb88302/

💖 Support This Project
If you found this project helpful,

please consider giving it a ⭐ on GitHub.

It motivates me to build more AI and Machine Learning projects.

🙏 Acknowledgements
Special thanks to the open-source community and the developers of:

Python
Streamlit
Ollama
⭐ If you like this project, don't forget to Star the Repository! ⭐
Made with ❤️ using Python, Streamlit and Ollama.

© 2026 Emaan Aftab. All Rights Reserved.
