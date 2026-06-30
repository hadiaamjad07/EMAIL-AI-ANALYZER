# ==========================================================
# AI EMAIL ANALYZER
# ==========================================================
import streamlit as st
import datetime

from email_reader import parse_eml_bytes, parse_pasted_text, extract_email_address
from risk_scoring import score_email
from analyzer import check_ollama, get_models, generate_response, cached_generate, truncate
from prompt import (
    email_summary_prompt,
    phishing_analysis_prompt,
    reply_draft_prompt,
    keyword_prompt,
    thread_summary_prompt,
)

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="AI Email Analyzer",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
.stApp { background-color:#0E1117; color:white; }
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
[data-testid="stSidebar"] { background-color:#161B22; }
.stButton>button {
    width:100%; background:#2563EB; color:white;
    border-radius:8px; border:none;
}
.stButton>button:hover { background:#1D4ED8; }
[data-testid="stFileUploader"] {
    border:2px dashed #2563EB; border-radius:10px; padding:15px;
}
.risk-high { background:#3F1D1D; border-left:5px solid #EF4444; padding:14px; border-radius:8px; }
.risk-medium { background:#3F2E14; border-left:5px solid #F59E0B; padding:14px; border-radius:8px; }
.risk-low { background:#3A3A14; border-left:5px solid #EAB308; padding:14px; border-radius:8px; }
.risk-none { background:#16322A; border-left:5px solid #22C55E; padding:14px; border-radius:8px; }
.keyword-chip {
    background:#1F2937; padding:10px; border-radius:8px;
    margin-bottom:8px; border-left:5px solid #2563EB;
}
.header-card {
    background:#161B22; padding:14px 18px; border-radius:10px; margin-bottom:10px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# SESSION STATE
# -----------------------------
if "current_email" not in st.session_state:
    st.session_state.current_email = None
if "thread_emails" not in st.session_state:
    st.session_state.thread_emails = []

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.title("📧 Email Analyzer")

    ollama_up = check_ollama()
    if ollama_up:
        st.success("🟢 Ollama Online")
    else:
        st.error("🔴 Ollama Offline")
        st.info("Run: `ollama serve` in your terminal, then refresh.")

    st.markdown("---")
    st.write("### AI Model")
    models = get_models()
    selected_model = st.selectbox("Choose Model", models)

    st.markdown("---")
    st.write("### Input Method")
    input_method = st.radio(
        "How do you want to provide the email?",
        ["Upload .eml file", "Paste email text"],
        label_visibility="collapsed",
    )

    st.markdown("---")
    st.write("### Features")
    st.write("📝 Summary & Intent  ·  🚩 Phishing/Spam Risk")
    st.write("✍️ Reply Drafting  ·  🔑 Keywords")
    st.write("🧵 Thread Summary")

    st.markdown("---")
    if st.button("🗑️ Clear Thread"):
        st.session_state.thread_emails = []
        st.rerun()

# -----------------------------
# MAIN PAGE
# -----------------------------
st.title("📧 AI Email Analyzer")
st.subheader("Summarize, assess risk, and draft replies — all running locally")
st.divider()

tab_single, tab_thread = st.tabs(["📨 Single Email", "🧵 Email Thread"])

# ======================================================
# TAB 1 — SINGLE EMAIL ANALYSIS
# ======================================================
with tab_single:
    email_data = None
    parse_error = None

    if input_method == "Upload .eml file":
        uploaded_file = st.file_uploader("Choose an .eml file", type=["eml"])
        if uploaded_file is not None:
            email_data, parse_error = parse_eml_bytes(uploaded_file.read())
    else:
        pasted = st.text_area(
            "Paste the email here (headers like From/Subject/Date are optional)",
            height=250,
            placeholder="From: jane@example.com\nSubject: Project update\n\nHi team, ...",
        )
        if st.button("📥 Load Pasted Email") and pasted.strip():
            email_data, parse_error = parse_pasted_text(pasted)
            st.session_state.current_email = email_data

    if email_data:
        st.session_state.current_email = email_data

    email_data = st.session_state.current_email

    if parse_error:
        st.error(f"⚠️ {parse_error}")

    if email_data:
        body = truncate(email_data.get("body", ""))

        st.markdown(f"""
        <div class="header-card">
        <b>From:</b> {email_data.get('from', 'Unknown')}<br>
        <b>To:</b> {email_data.get('to', 'Unknown')}<br>
        <b>Subject:</b> {email_data.get('subject', 'Unknown')}<br>
        <b>Date:</b> {email_data.get('date', 'Unknown')}
        </div>
        """, unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("📝 Word Count", len(body.split()))
        with c2:
            st.metric("🔗 Links Found", len(email_data.get("links", [])))
        with c3:
            st.metric("📎 Attachments", len(email_data.get("attachments", [])))

        if email_data.get("attachments"):
            with st.expander("📎 Attachments"):
                for att in email_data["attachments"]:
                    st.write(f"- {att['name']} ({att['size_kb']} KB)")

        if email_data.get("links"):
            with st.expander(f"🔗 Links Found ({len(email_data['links'])})"):
                for link in email_data["links"]:
                    st.write(f"- {link}")

        with st.expander("📄 View Full Email Body", expanded=False):
            st.text_area("Body", body, height=250, key="view_body")

        if not body.strip():
            st.warning("No email body text could be extracted.")
        else:
            st.divider()
            st.subheader("🚩 Phishing / Spam Risk Check")
            risk = score_email(email_data)

            css_class = {
                "🔴 High Risk": "risk-high",
                "🟠 Medium Risk": "risk-medium",
                "🟡 Low Risk": "risk-low",
                "🟢 No Red Flags Detected": "risk-none",
            }.get(risk["level"], "risk-none")

            reasons_html = "".join(f"<li>{r}</li>" for r in risk["reasons"])
            st.markdown(f"""
            <div class="{css_class}">
            <b>{risk['level']}</b> — Heuristic Score: {risk['score']}/100
            <ul>{reasons_html}</ul>
            </div>
            """, unsafe_allow_html=True)

            if st.button("🛡️ Get AI Second Opinion on Risk", disabled=not ollama_up):
                with st.spinner("AI is reviewing this email for risk signals..."):
                    result = cached_generate(
                        phishing_analysis_prompt(email_data, risk), selected_model
                    )
                if result.startswith("[Error]"):
                    st.error(result)
                else:
                    st.markdown(result)

            st.divider()
            st.subheader("🤖 AI Summary & Intent")
            if st.button("🚀 Analyze Email", disabled=not ollama_up):
                with st.spinner("Analyzing email..."):
                    summary = generate_response(
                        email_summary_prompt(email_data), selected_model
                    )
                if summary.startswith("[Error]"):
                    st.error(summary)
                else:
                    st.markdown(summary)
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
                    st.download_button(
                        "📥 Download Analysis (.txt)",
                        data=summary,
                        file_name=f"Email_Analysis_{timestamp}.txt",
                        mime="text/plain",
                    )

            st.divider()
            st.subheader("🔑 Keywords")
            if st.button("Extract Keywords", disabled=not ollama_up):
                with st.spinner("Extracting keywords..."):
                    kw_result = cached_generate(keyword_prompt(body), selected_model)
                if kw_result.startswith("[Error]"):
                    st.error(kw_result)
                else:
                    for kw in [k.strip() for k in kw_result.split("\n") if k.strip()]:
                        st.markdown(f'<div class="keyword-chip">🔹 <b>{kw}</b></div>', unsafe_allow_html=True)

            st.divider()
            st.subheader("✍️ Draft a Reply")
            rc1, rc2 = st.columns([1, 2])
            with rc1:
                tone = st.selectbox(
                    "Reply tone",
                    ["Professional", "Friendly", "Apologetic", "Firm / Direct", "Brief"],
                )
            with rc2:
                custom_instr = st.text_input(
                    "Optional instructions (e.g. 'decline politely', 'ask for a deadline extension')"
                )

            if st.button("✍️ Generate Reply Draft", disabled=not ollama_up):
                with st.spinner("Drafting reply..."):
                    draft = cached_generate(
                        reply_draft_prompt(email_data, tone, custom_instr), selected_model
                    )
                if draft.startswith("[Error]"):
                    st.error(draft)
                else:
                    st.text_area("Draft Reply", draft, height=200)
                    st.download_button(
                        "📥 Download Draft (.txt)",
                        data=draft,
                        file_name="Reply_Draft.txt",
                        mime="text/plain",
                    )
    else:
        st.info("⬆️ Upload an .eml file or paste an email above to begin.")

# ======================================================
# TAB 2 — EMAIL THREAD SUMMARY
# ======================================================
with tab_thread:
    st.write("Add multiple messages from a thread (paste each one), then get a combined summary.")

    thread_input = st.text_area(
        "Paste one message from the thread",
        height=180,
        key="thread_input_box",
    )
    if st.button("➕ Add Message to Thread") and thread_input.strip():
        parsed, err = parse_pasted_text(thread_input)
        if err:
            st.error(err)
        else:
            st.session_state.thread_emails.append(parsed)
            st.rerun()

    if st.session_state.thread_emails:
        st.write(f"**{len(st.session_state.thread_emails)} message(s) in thread:**")
        for i, msg in enumerate(st.session_state.thread_emails, 1):
            with st.expander(f"Message {i}: {msg.get('subject', 'No subject')} — {msg.get('from', 'Unknown')}"):
                st.write(msg.get("body", ""))

        if st.button("🧵 Summarize Thread", disabled=not ollama_up):
            combined = "\n\n---\n\n".join(
                f"From: {m.get('from')}\nSubject: {m.get('subject')}\n\n{m.get('body')}"
                for m in st.session_state.thread_emails
            )
            combined = truncate(combined, limit=10000)
            with st.spinner("Summarizing thread..."):
                result = generate_response(thread_summary_prompt(combined), selected_model)
            if result.startswith("[Error]"):
                st.error(result)
            else:
                st.markdown(result)
    else:
        st.info("Add at least one message to build a thread summary.")