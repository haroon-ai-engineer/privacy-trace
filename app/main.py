from fastapi import FastAPI

from app.models.request import ScanRequest

from app.detectors.registry import DetectorRegistry
from app.detectors.email_detector import EmailDetector
from app.detectors.detector_engine import DetectionEngine
from app.detectors.phone_detector import PhoneDetector

app = FastAPI(
    title="Privacy Trace API",
    version="0.1.0",
    description="Backend API for detecting PII in AI prompts."
)

registry = DetectorRegistry()

registry.register(EmailDetector())
registry.register(PhoneDetector())

engine = DetectionEngine(registry)


@app.get("/")
def root():
    return {"message": "Welcome to Privacy Trace API 🚀"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/scan")
def scan_text(request: ScanRequest):
    findings = engine.scan(request.text)

    return {
        "success": True,
        "findings": findings,
    }