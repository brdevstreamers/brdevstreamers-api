from typing import Optional
from pydantic import BaseModel

class UpdateUserViewModel(BaseModel):
    user_login: str
    email: str
    bio: Optional[str]
    discord: Optional[str]
    instagram: Optional[str]
    linkedin: Optional[str]
    github: Optional[str]
    twitter: Optional[str]

class UserOutViewModel(BaseModel):
    user_login: Optional[str]
    email: Optional[str]
    bio: Optional[str]
    github_url: Optional[str]
    twitter_url: Optional[str]
    instagram_url: Optional[str]
    linkedin_url: Optional[str]
    discord_url: Optional[str]    