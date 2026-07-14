from app.detectors.email_detector import detect_emails
from app.models.finding import Finding


def run_all_detectors(text: str) -> list[Finding]:
    findings: list[Finding] = []

    findings.extend(detect_emails(text))

    return findings