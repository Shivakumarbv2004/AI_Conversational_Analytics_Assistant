from pydantic import BaseModel
from typing import Any


class ChatResponse(BaseModel):
    success: bool
    question: str
    answer: str


class AnalyticsResponse(BaseModel):
    success: bool
    tool: str
    result: Any