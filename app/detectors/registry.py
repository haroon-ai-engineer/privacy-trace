from app.detectors.base import BaseDetector


class DetectorRegistry:
    def __init__(self) -> None:
        self._detectors: list[BaseDetector] = []

    def register(self, detector: BaseDetector) -> None:
        self._detectors.append(detector)

    def get_detectors(self) -> list[BaseDetector]:
        return self._detectors