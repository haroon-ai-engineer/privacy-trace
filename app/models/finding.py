from pydantic import BaseModel


class Finding(BaseModel):
    type: str
    value: str
    start: int
    end: int
    severity: str