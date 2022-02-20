from typing import Optional
from xmlrpc.client import DateTime
from datetime import datetime
from pydantic import BaseModel


class StatViewModel(BaseModel):
    user_login:str
    access_date: datetime
    type: str
    fingerprint: str