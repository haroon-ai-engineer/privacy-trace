import re

from app.models.finding import Finding


EMAIL_PATTERN = re.compile(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
)


def detect_emails(text: str) -> list[Finding]:
    findings = []

    for match in EMAIL_PATTERN.finditer(text):
        findings.append(
            Finding(
                type="EMAIL",
                value=match.group(),
                start=match.start(),
                end=match.end(),
                severity="Medium",
            )
        )

    return findings