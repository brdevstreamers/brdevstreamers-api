import unittest
from unittest.mock import MagicMock, Mock, patch
from dotenv import load_dotenv
import pytest
from twitchAPI.twitch import Twitch

from service.twitch_service import TwitchService


class TestTwitchService(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        

    def mock_twitch(self):
        twitch = Mock()
        response = {
            "data": [
                {
                    "id": "44960190524",
                    "user_id": "166681140",
                    "user_login": "marcobrunodev",
                    "user_name": "MarcoBrunoDev",
                    "game_id": "1469308723",
                    "game_name": "Software and Game Development",
                    "type": "live",
                    "title": "#28 Pet Snoar | Pet Runner | !Alura",
                    "viewer_count": 158,
                    "started_at": "2022-03-14T11:00:48Z",
                    "language": "pt",
                    "thumbnail_url": "https://static-cdn.jtvnw.net/previews-ttv/live_user_marcobrunodev-{width}x{height}.jpg",
                    "tag_ids": [
                        "39ee8140-901a-4762-bfca-8260dea1310f",
                        "a106f013-6e26-4f27-9a4b-01e9d76084e2",
                        "6e23d976-33ec-47e8-b22b-3727acd41862",
                        "f588bd74-e496-4d11-9169-3597f38a5d25",
                        "6f86127d-6051-4a38-94bb-f7b475dde109",
                        "c23ce252-cf78-4b98-8c11-8769801aaf3a",
                    ],
                    "is_mature": 'false',
                }
            ],
            "pagination": {
                "cursor": "eyJiIjp7IkN1cnNvciI6ImV5SnpJam94TlRndU1URXdOVEl3TlRreE9UZzFNRGdzSW1RaU9tWmhiSE5sTENKMElqcDBjblZsZlE9PSJ9LCJhIjp7IkN1cnNvciI6IiJ9fQ"
            },
        }
        twitch.get_streams = MagicMock(return_value=response)

        streamer = {"data": [{"profile_image_url": '', 'description': ''}]}
        twitch.get_users = MagicMock(return_value=streamer)
        return twitch

    def test_get_streamers(self):
        twitch_service = TwitchService(self.mock_twitch())
        streamers = twitch_service.get_streamers()
        self.assertEqual(len(streamers), 1)
        self.assertEqual(streamers[0].user_login, "marcobrunodev")
