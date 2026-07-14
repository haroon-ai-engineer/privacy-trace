from abc import ABC, abstractmethod

from app.models.finding import Finding


class BaseDetector(ABC):
    """
    Base class for all PII detectors.
    """

    @abstractmethod
    def scan(self, text: str) -> list[Finding]:
        """
        Scan text and return detected findings.
        """
        pass