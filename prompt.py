"""
prompt.py
Prompt templates for the AI Email Analyzer.
"""


def email_summary_prompt(email_data):
    return f"""You are an AI Email Analyst.
Analyze the email below and return your answer in this exact format:

📄 Summary:
2-3 sentence summary of what this email is about.

🎯 Intent:
What does the sender want from the recipient? (e.g. request, FYI, sales pitch, complaint, scheduling)

😊 Tone:
Formal / Casual / Aggressive / Friendly / Urgent / Neutral (pick the best fit, one line)

⏰ Urgency Level:
Low / Medium / High — with a one-line reason.

✅ Action Items:
- Action 1
- Action 2
(write "None found" if there are none)

📅 Mentioned Dates/Deadlines:
List any specific dates or deadlines mentioned, or "None found".

✅ Final Verdict:
One sentence: should this email be replied to urgently, replied to later, or ignored/archived?

From: {email_data.get('from', 'Unknown')}
Subject: {email_data.get('subject', 'Unknown')}

Email Body:
{email_data.get('body', '')}"""


def phishing_analysis_prompt(email_data, heuristic_result):
    return f"""You are a cybersecurity analyst reviewing a potentially suspicious email.

A rule-based scanner already found this:
Risk Score: {heuristic_result['score']}/100 ({heuristic_result['level']})
Flags: {", ".join(heuristic_result['reasons'])}

Now read the actual email content yourself and give a second opinion.

Return your answer in this format:

🛡️ Your Assessment:
Legitimate / Suspicious / Likely Phishing — one line.

🔍 What stands out:
- Point 1
- Point 2
- Point 3

💡 Recommendation:
One or two sentences telling the recipient what to do (e.g. verify sender via official channel, do not click links, report as phishing, safe to proceed).

From: {email_data.get('from', 'Unknown')}
Subject: {email_data.get('subject', 'Unknown')}

Email Body:
{email_data.get('body', '')}"""


def reply_draft_prompt(email_data, tone="Professional", custom_instructions=""):
    extra = f"\nAdditional instructions from the user: {custom_instructions}" if custom_instructions else ""
    return f"""You are helping draft a reply to the email below.
Write a {tone.lower()} reply.
Keep it concise and natural — do not over-explain.
Do not invent facts not present in the original email.
Sign off generically (e.g. "Best regards") without inventing a name unless one is given.
{extra}

Original Email:
From: {email_data.get('from', 'Unknown')}
Subject: {email_data.get('subject', 'Unknown')}

{email_data.get('body', '')}

Write only the reply email body, nothing else."""


def keyword_prompt(text):
    return f"""Extract the 8 most important keywords or key phrases from this email.
Rules:
- Only keywords/phrases.
- One per line.
- No numbering or bullet points.
- Maximum 3 words per keyword.

Email:
{text}"""


def thread_summary_prompt(combined_text):
    return f"""You are summarizing an email thread (multiple back-and-forth messages).

Return:

📄 Thread Summary:
What is this conversation about overall, and how did it progress?

👥 Participants & Positions:
Briefly note what each participant seems to want or argue.

✅ Current Status / Next Step:
What needs to happen next, and who owns it?

Thread:
{combined_text}"""