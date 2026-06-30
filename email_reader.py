"""
email_reader.py
Parsing helpers for the AI Email Analyzer.
"""

import email
from email import policy
from email.utils import parseaddr, parsedate_to_datetime
import re


def parse_eml_bytes(raw_bytes):
    """Parse raw .eml bytes into a structured dict. Returns (data, error)."""
    try:
        msg = email.message_from_bytes(raw_bytes, policy=policy.default)
        return _structure_message(msg), None
    except Exception as e:
        return None, f"Failed to parse .eml file: {e}"


def parse_pasted_text(text):
    """
    Parse pasted email text. Tries to detect headers (From/To/Subject/Date)
    at the top; falls back to treating everything as body text.
    """
    header_pattern = re.compile(
        r'^(From|To|Cc|Bcc|Subject|Date|Reply-To)\s*:\s*(.*)$',
        re.IGNORECASE,
    )
    lines = text.split("\n")
    headers = {}
    body_start = 0

    for i, line in enumerate(lines):
        match = header_pattern.match(line.strip())
        if match:
            key = match.group(1).title()
            headers[key] = match.group(2).strip()
            body_start = i + 1
        elif line.strip() == "" and headers:
            body_start = i + 1
            break
        elif not headers and line.strip() != "":
            body_start = 0
            break

    body = "\n".join(lines[body_start:]).strip()
    if not body and not headers:
        body = text.strip()

    data = {
        "from": headers.get("From", "Not Found"),
        "to": headers.get("To", "Not Found"),
        "cc": headers.get("Cc", "Not Found"),
        "subject": headers.get("Subject", "Not Found"),
        "date": headers.get("Date", "Not Found"),
        "reply_to": headers.get("Reply-To", "Not Found"),
        "body": body,
        "attachments": [],
        "links": _extract_links(body),
        "raw_header_count": len(headers),
    }
    return data, None


def _structure_message(msg):
    subject = msg.get("Subject", "Not Found")
    from_addr = msg.get("From", "Not Found")
    to_addr = msg.get("To", "Not Found")
    cc_addr = msg.get("Cc", "Not Found")
    reply_to = msg.get("Reply-To", "Not Found")
    date_raw = msg.get("Date", "Not Found")

    try:
        date_parsed = parsedate_to_datetime(date_raw) if date_raw != "Not Found" else None
        date_display = date_parsed.strftime("%Y-%m-%d %H:%M %Z") if date_parsed else date_raw
    except Exception:
        date_display = date_raw

    body = ""
    attachments = []

    if msg.is_multipart():
        for part in msg.walk():
            content_disposition = str(part.get("Content-Disposition", ""))
            content_type = part.get_content_type()

            if "attachment" in content_disposition:
                filename = part.get_filename() or "unnamed_attachment"
                size = len(part.get_payload(decode=True) or b"")
                attachments.append({"name": filename, "size_kb": round(size / 1024, 1)})
            elif content_type == "text/plain" and not body:
                try:
                    body = part.get_content()
                except Exception:
                    payload = part.get_payload(decode=True)
                    body = payload.decode(errors="replace") if payload else ""
            elif content_type == "text/html" and not body:
                html = ""
                try:
                    html = part.get_content()
                except Exception:
                    payload = part.get_payload(decode=True)
                    html = payload.decode(errors="replace") if payload else ""
                body = _strip_html(html)
    else:
        try:
            body = msg.get_content()
        except Exception:
            payload = msg.get_payload(decode=True)
            body = payload.decode(errors="replace") if payload else str(msg.get_payload())
        if msg.get_content_type() == "text/html":
            body = _strip_html(body)

    return {
        "from": from_addr,
        "to": to_addr,
        "cc": cc_addr,
        "subject": subject,
        "date": date_display,
        "reply_to": reply_to,
        "body": body.strip(),
        "attachments": attachments,
        "links": _extract_links(body),
        "raw_header_count": len(msg.items()),
    }


def _strip_html(html):
    """Very lightweight HTML-to-text fallback (no external deps)."""
    text = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'</p>', '\n\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'&nbsp;', ' ', text)
    text = re.sub(r'&amp;', '&', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def _extract_links(text):
    return re.findall(r'https?://[^\s<>"\')\]]+', text or "")


def extract_email_address(header_value):
    """Pull the bare email address out of a 'Name <email>' style header."""
    if not header_value or header_value == "Not Found":
        return "Not Found"
    name, addr = parseaddr(header_value)
    return addr or header_value