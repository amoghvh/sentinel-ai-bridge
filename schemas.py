from pydantic import BaseModel, Field
from typing import List, Optional

class SanitizeRequest(BaseModel):
    text: str = Field(..., description="The sensitive text to be analyzed and redacted.")

class SanitizeResponse(BaseModel):
    sanitized_text: str
    entities_found: List[str]
    audit_id: str
    timestamp: str