from typing import Optional
from pydantic import BaseModel


class UserViewModel(BaseModel):
    user_login: str
    email: str
    bio: Optional[str]
    discord: Optional[str]
    instagram: Optional[str]
    linkedin: Optional[str]
    github: Optional[str]
    twitter: Optional[str]