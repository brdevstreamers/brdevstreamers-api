from typing import Optional
from xmlrpc.client import DateTime
from datetime import datetime
from pydantic import BaseModel


class StatViewModel(BaseModel):
    user_login:str
    target_user:Optional[str]
    date: datetime
    type: str
    interaction_fingerprint: str