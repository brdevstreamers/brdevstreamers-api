from typing import Optional

from view_model.user_viewmodel import UserViewModel

class StreamViewModel(UserViewModel):
    id: Optional[str]
    user_id: Optional[str]
    user_name: Optional[str]
    title: Optional[str]
    viewer_count: Optional[int]
    started_at: Optional[str]
    thumbnail_url: Optional[str]
    profile_image_url: Optional[str]
    description: Optional[str]