"""
risk_scoring.py
Lightweight, rule-based heuristics to flag suspicious / phishing-like emails.
"""

import re

URGENCY_WORDS = [
    "urgent", "immediately", "act now", "verify your account", "suspended",
    "limited time", "act fast", "final notice", "click here", "confirm your password",
    "unauthorized access", "your account has been", "claim your", "winner",
    "congratulations you", "wire transfer", "gift card", "bitcoin", "crypto payment",
]

SENSITIVE_REQUESTS = [
    "password", "social security", "ssn", "credit card", "bank account",
    "routing number", "otp", "one-time code", "verification code", "pin number",
]

SUSPICIOUS_TLDS = [".ru", ".tk", ".top", ".xyz", ".click", ".info", ".work"]

MISMATCH_DOMAIN_BRANDS = [
    "paypal", "amazon", "microsoft", "apple", "netflix", "bank", "irs",
    "google", "facebook", "instagram", "linkedin",
]


def score_email(data):
    """
    Returns a dict: {score (0-100), level, reasons: [...]}
    Higher score = higher suspicion.
    """
    reasons = []
    score = 0

    body = (data.get("body") or "").lower()
    subject = (data.get("subject") or "").lower()
    from_addr = (data.get("from") or "").lower()
    links = data.get("links", [])

    hits = [w for w in URGENCY_WORDS if w in body or w in subject]
    if hits:
        score += min(30, 6 * len(hits))
        reasons.append(f"Urgency/pressure language detected: {', '.join(hits[:5])}")

    hits = [w for w in SENSITIVE_REQUESTS if w in body]
    if hits:
        score += min(25, 8 * len(hits))
        reasons.append(f"Requests sensitive information: {', '.join(hits[:5])}")

    if links:
        suspicious_links = [l for l in links if any(tld in l.lower() for tld in SUSPICIOUS_TLDS)]
        if suspicious_links:
            score += 20
            reasons.append(f"Contains link(s) with suspicious domain extensions ({len(suspicious_links)})")
        if len(links) > 5:
            score += 10
            reasons.append(f"Unusually high number of links ({len(links)})")

    for brand in MISMATCH_DOMAIN_BRANDS:
        if brand in subject or brand in body[:300]:
            if brand not in from_addr:
                score += 15
                reasons.append(
                    f"Mentions '{brand}' but sender address doesn't appear to be from {brand}'s domain"
                )
                break

    if re.search(r'dear (customer|user|valued|sir/madam)', body):
        score += 10
        reasons.append("Generic greeting instead of personalized name")

    reply_to = (data.get("reply_to") or "").lower()
    if reply_to and reply_to != "not found" and from_addr and reply_to != from_addr:
        if "@" in reply_to and "@" in from_addr:
            reply_domain = reply_to.split("@")[-1].strip(">").strip()
            from_domain = from_addr.split("@")[-1].strip(">").strip()
            if reply_domain != from_domain:
                score += 15
                reasons.append("Reply-To domain differs from From domain")

    score = min(100, score)

    if score >= 60:
        level = "🔴 High Risk"
    elif score >= 30:
        level = "🟠 Medium Risk"
    elif score > 0:
        level = "🟡 Low Risk"
    else:
        level = "🟢 No Red Flags Detected"

    if not reasons:
        reasons.append("No common phishing/spam patterns detected by the heuristic scan.")

    return {"score": score, "level": level, "reasons": reasons}