from pydantic import BaseModel

from app.core.enums import PIIType, Severity


class Finding(BaseModel):
    type: PIIType
    value: str
    start: int
    end: int
    severity: Severity