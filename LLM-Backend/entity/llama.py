from pydantic import BaseModel
from typing import Optional


class LlamaResponse(BaseModel):
    status: int
    data: Optional[str]

class LlamaRequest(BaseModel):
    user_prompt: str
    system_prompt: str