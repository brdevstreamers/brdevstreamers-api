from typing import Optional

from pydantic import BaseModel


class StatsViewModel(BaseModel):
    user_login: Optional[str]
    stream_clicks: Optional[int]
    vod_clicks: Optional[int]
    preview_clicks: Optional[int]
