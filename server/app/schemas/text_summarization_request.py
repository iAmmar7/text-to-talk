from pydantic import BaseModel
from typing import Optional


class TextSummarizationRequest(BaseModel):
    text: str
    min_length: Optional[int] = 100
    max_length: Optional[int] = 1000
