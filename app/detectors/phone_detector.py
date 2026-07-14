import re

from app.core.enums import PIIType, Severity
from app.detectors.base import BaseDetector
from app.models.finding import Finding


class PhoneDetector(BaseDetector):
    """
    Detect international and local phone numbers.
    """

    PHONE_PATTERN = re.compile(
        r"\+?\d[\d\s\-()]{7,}\d"
    )

    def scan(self, text: str) -> list[Finding]:
        findings: list[Finding] = []

        for match in self.PHONE_PATTERN.finditer(text):
            findings.append(
                Finding(
                    type=PIIType.PHONE,
                    value=match.group(),
                    start=match.start(),
                    end=match.end(),
                    severity=Severity.MEDIUM,
                )
            )

        return findings