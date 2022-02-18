from typing import Optional
from pydantic import BaseModel


class StreamerViewModel(BaseModel):
    user_id:str
    user_login: str
    discord: Optional[str]
    instagram: Optional[str]
    linkedin: Optional[str]
    github: Optional[str]
    twitter: Optional[str]