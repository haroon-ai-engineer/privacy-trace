from fastapi import FastAPI

from app.models.request import ScanRequest
from app.detectors.detector_engine import run_all_detectors

app = FastAPI(
    title="Privacy Trace API",
    version="0.1.0",
    description="Backend API for detecting PII in AI prompts."
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Privacy Trace API 🚀"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/scan")
def scan_text(request: ScanRequest):
    findings = run_all_detectors(request.text)

    return {
        "success": True,
        "findings": findings,
    }