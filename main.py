from fastapi import FastAPI
from schemas import SanitizeRequest, SanitizeResponse
from engine import SentinelEngine

# Initializing the app with a professional title
app = FastAPI(title="Sentinel-AI Privacy Bridge")
engine = SentinelEngine()

@app.post("/sanitize", response_model=SanitizeResponse)
async def sanitize_text(request: SanitizeRequest):
    """
    Core endpoint for PII redaction.
    Takes raw text and returns a sanitized version with an audit trail.
    """
    return engine.scan_and_redact(request.text)

@app.get("/health")
def health_check():
    """Service heartbeat for monitoring."""
    return {"status": "operational", "engine": "active"}