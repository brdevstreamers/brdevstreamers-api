from datetime import datetime
from typing import Optional
from xmlrpc.client import DateTime

from pydantic import BaseModel


class UserInteractionViewModel(BaseModel):
    user_login: str
    target_user: Optional[str]
    date: datetime
    type: str
    interaction_fingerprint: str
