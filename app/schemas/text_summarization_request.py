from pydantic import BaseModel
from typing import Optional


class TextSummarizationRequest(BaseModel):
    text: str
    min_length: Optional[int] = 30
    max_length: Optional[int] = 1000
