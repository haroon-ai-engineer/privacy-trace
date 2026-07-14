from app.detectors.registry import DetectorRegistry
from app.models.finding import Finding


class DetectionEngine:
    def __init__(self, registry: DetectorRegistry) -> None:
        self.registry = registry

    def scan(self, text: str) -> list[Finding]:
        findings: list[Finding] = []

        for detector in self.registry.get_detectors():
            findings.extend(detector.scan(text))

        return findings