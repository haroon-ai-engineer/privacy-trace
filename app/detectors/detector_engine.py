from app.detectors.email_detector import EmailDetector
from app.models.finding import Finding


class DetectionEngine:
    def __init__(self) -> None:
        self.detectors = [
            EmailDetector(),
        ]

    def scan(self, text: str) -> list[Finding]:
        findings: list[Finding] = []

        for detector in self.detectors:
            findings.extend(detector.scan(text))

        return findings