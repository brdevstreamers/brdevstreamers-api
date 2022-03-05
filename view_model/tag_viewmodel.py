from typing import Optional

from pydantic import BaseModel


class TagViewModel(BaseModel):
    name:Optional[str]
    id:Optional[str]