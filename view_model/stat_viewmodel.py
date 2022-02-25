from datetime import datetime

from pydantic import BaseModel


class StatViewModel(BaseModel):
    user_login:str
    access_date: datetime
    type: str
    fingerprint: str