import re

from app.core.enums import PIIType, Severity
from app.detectors.base import BaseDetector
from app.models.finding import Finding


class EmailDetector(BaseDetector):
    EMAIL_PATTERN = re.compile(
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    )

    def scan(self, text: str) -> list[Finding]:
        findings: list[Finding] = []

        for match in self.EMAIL_PATTERN.finditer(text):
            findings.append(
                Finding(
                    type=PIIType.EMAIL,
                    value=match.group(),
                    start=match.start(),
                    end=match.end(),
                    severity=Severity.MEDIUM,
                )
            )

        return findings