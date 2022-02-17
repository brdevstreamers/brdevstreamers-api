from pydantic import BaseModel


class StreamerViewModel(BaseModel):
    user_id:str
    user_login: str
    discord: str
    instagram: str
    linkedin: str
    github: str
    twitter: str