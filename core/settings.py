from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    ENV: str = "dev"
    API_TOKEN: str

    # Twitch settings.
    CLIENT_ID: str
    CLIENT_SECRET: str

    # Twitter settings.
    TWITTER_API_KEY: str
    TWITTER_API_SECRET: str
    TWITTER_ACCESS_TOKEN: str
    TWITTER_ACCESS_SECRET: str

    # GitHub settings.
    GITHUB_TOKEN: str

    # Production only.
    CERT: Optional[str]
    PRIVATE_KEY: Optional[str]

    # The database location
    DB: str = ""
