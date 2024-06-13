from pydantic import BaseModel, ConfigDict, Field
from typing import List, Tuple, Optional


class LlamaResponse(BaseModel):
    status: int
    data: Optional[str]

class LlamaRequest(BaseModel):
    user_prompt: str
    system_prompt: str