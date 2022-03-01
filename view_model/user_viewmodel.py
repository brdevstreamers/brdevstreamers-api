from typing import Optional
from pydantic import BaseModel


class UserViewModel(BaseModel):
    user_login: Optional[str]
    email: Optional[str]
    bio: Optional[str]
    github_url: Optional[str]
    twitter_url: Optional[str]
    instagram_url: Optional[str]
    linkedin_url: Optional[str]
    discord_url: Optional[str]