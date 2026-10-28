import re
from typing import Any

def analyze(category: str, text: str, sender: str = "", url: str = "") -> dict[str, Any]:
    combined = f"{text} {sender} {url}".lower()
    findings: list[dict[str, str]] = []
    def add(condition: bool, title: str, explanation: str, severity: str) -> None:
        if condition:
            findings.append({"title": title, "explanation": explanation, "severity": severity})
    add(bool(re.search(r"\b(otp|one.time password|verification code|recovery code|password)\b", combined)),
        "Credential or code request", "Requests for passwords, OTPs, or recovery codes are warning signs. Do not share them.", "high")
    add(bool(re.search(r"\b(urgent|immediately|last chance|account.{0,20}(closed|blocked|suspended))\b", combined)),
        "Urgency or threat of loss", "Pressure to act quickly can prevent careful verification. Pause and verify independently.", "medium")
    add(bool(re.search(r"\b(scholarship|prize|winner|free money|refund|grant|reward)\b", combined)),
        "Unexpected benefit claim", "Unexpected benefits should be checked through an independently obtained official channel.", "medium")
    add(bool(re.search(r"\b(send|transfer|pay|payment|upi|bank details|gift card)\b", combined)),
        "Payment or money request", "Verify unexpected money requests through a separate trusted channel.", "high")
    add(bool(re.search(r"https?://|www\.|bit\.ly|tinyurl|t\.co", combined)),
        "URL or link mentioned", "A link alone is not proof of a scam. Do not open unexpected links; navigate to the official service yourself.", "medium")
    add(category == "Fake account / impersonation" or bool(re.search(r"\b(fake account|impersonat|using my photo|copied my profile)\b", combined)),
        "Possible impersonation", "Preserve the profile URL and relevant messages, verify independently, and use official platform reporting.", "high")
    add(category == "Cyberbullying / harassment" or bool(re.search(r"\b(cyberbully|harass|threaten|threat|humiliat|abusive|blackmail)\b", combined)),
        "Harassment or threatening language", "Avoid retaliation, preserve context if safe, and seek trusted support. Immediate safety comes first.", "high")
    add(category == "Account compromise" or bool(re.search(r"\b(unrecognized login|unknown login|account hacked|compromised|suspicious login)\b", combined)),
        "Possible account compromise", "Use the provider's official app/site from a trusted device, secure the account, enable MFA, and review sessions.", "high")
    score = min(100, sum(35 if f["severity"] == "high" else 18 for f in findings)) if findings else None
    risk = "Unable to determine" if score is None else ("High concern — take protective steps" if score >= 55 else "Suspicious — verify first" if score >= 20 else "Low apparent risk")
    actions = [
        "Pause before responding; do not click unexpected links or share credentials, OTPs, recovery codes, or payment details.",
        "Verify the claim using an official website or contact method obtained independently.",
        "Seek trusted assistance if the situation remains unclear."
    ]
    if category == "Cyberbullying / harassment":
        actions = ["Do not retaliate. Preserve relevant messages and context if safe.", "Use official platform reporting/blocking tools as appropriate.", "Seek trusted support; for immediate danger, contact appropriate local emergency support."]
    elif category == "Fake account / impersonation":
        actions = ["Verify the identity independently.", "Preserve the profile URL, relevant messages, and timestamps.", "Report through the platform's official process; warn affected contacts through a trusted channel if appropriate."]
    elif category == "Account compromise":
        actions = ["Open the provider's official app/site directly from a trusted device.", "Change the password if safe, enable MFA, and review active sessions.", "Use the provider's official account recovery process."]
    return {
        "risk": risk, "score": score, "findings": findings, "actions": actions,
        "preserve": ["Original message and sender/account identifier", "Date and approximate time observed",
                     "URL/profile reference copied as text; do not open it", "Relevant screenshot/file references if already safely captured",
                     "Actions taken and any report reference"],
        "avoid": ["Do not share passwords, OTPs, recovery codes, or payment details.", "Do not retaliate or expose private information publicly."],
        "uncertainty": ("Rule-based indicators were found. Context matters; this is not proof of malicious intent."
                        if findings else "No configured indicators were detected, or the description is too limited. This does not prove safety.")
    }
