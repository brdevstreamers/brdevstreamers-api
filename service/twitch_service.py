import json
import os
from random import shuffle
from typing import List

from twitchAPI.twitch import Twitch
from twitchAPI.types import TimePeriod

# from model.user_model import User
# from persistence.user_dao import get_users_by_name
from view_model.stream_viewmodel import StreamViewModel
from view_model.tag_viewmodel import TagViewModel
from view_model.vod_viewmodel import VodViewModel


class TwitchService:

    config, twitch = None, None

    def __init__(self, twitch):
        self.twitch = twitch

    def get_streamers(self) -> List[StreamViewModel]:
        streams = self.twitch.get_streams(language="pt", game_id="1469308723")
        streams_model: List[StreamViewModel] = []
        stream_users = []
        for s in streams["data"]:
            stream = StreamViewModel()
            stream.id = s["id"]
            stream.user_id = s["user_id"]
            stream.user_name = s["user_name"]
            stream.user_login = s["user_login"]
            stream.title = s["title"]
            stream.viewer_count = s["viewer_count"]
            stream.started_at = s["started_at"]
            stream.thumbnail_url = s["thumbnail_url"]

            stream.tags = s["tag_ids"]

            streamer = self.get_streamer(s["user_id"])
            stream.profile_image_url = streamer["profile_image_url"]
            stream.description = streamer["description"][:100] + "..."

            stream_users.append(s["user_login"])
            streams_model.append(stream)

        # try:
        #     streamers = get_users_by_name(stream_users)
        #     for s in streamers:
        #         for stream in streams_model:
        #             if stream.user_login == s.user_login:
        #                 stream.github_url = s.github
        #                 stream.twitter_url = s.twitter
        #                 stream.instagram_url = s.instagram
        #                 stream.linkedin_url = s.linkedin
        #                 stream.discord_url = s.discord
        #                 stream.bio = s.bio
        #                 break
        # except Exception as e:
        #     print(e)
        shuffle(streams_model)
        return streams_model

    def get_streamer(self, id):
        return self.twitch.get_users(user_ids=[id])["data"][0]

    def get_vods(self) -> List[VodViewModel]:
        vods = self.twitch.get_videos(language="pt", game_id="1469308723", period=TimePeriod.DAY)
        vods_model: List[VodViewModel] = []
        vod_users = []

        for s in vods["data"]:
            if self.is_long_enough(s["duration"]):
                stream = VodViewModel()
                stream.id = s["id"]
                stream.user_id = s["user_id"]
                stream.user_name = s["user_name"]
                stream.user_login = s["user_login"]
                stream.title = s["title"]
                stream.viewer_count = s["view_count"]
                stream.started_at = s["published_at"]
                stream.thumbnail_url = s["thumbnail_url"]
                stream.stream_id = s["id"]
                stream.duration = s["duration"]

                streamer = self.get_streamer(s["user_id"])
                stream.profile_image_url = streamer["profile_image_url"]
                stream.description = streamer["description"][:100] + "..."

                vod_users.append(s["user_login"])
                vods_model.append(stream)
        # try:
        #     streamers = get_users_by_name(vod_users)
        #     for s in streamers:
        #         for stream in vods_model:
        #             if stream.user_login == s.user_login:
        #                 stream.github_url = s.github
        #                 stream.twitter_url = s.twitter
        #                 stream.instagram_url = s.instagram
        #                 stream.linkedin_url = s.linkedin
        #                 stream.discord_url = s.discord
        #                 stream.bio = s.bio
        #                 break
        # except Exception as e:
        #     print(e)
        return vods_model

    def is_long_enough(self, duration):
        return "h" in duration

    def get_tags(self) -> List[TagViewModel]:
        # streams = self.twitch.get_streams(language="pt", game_id="1469308723")
        # tag_ids = self.get_tag_list_from_streams(streams)
        # tags = self.twitch.get_all_stream_tags(tag_ids=tag_ids)
        # tags_dict = {}
        # for tag in tags["data"]:
        #     tag_model = TagViewModel(id=tag["tag_id"], name=tag["localization_names"]["pt-br"])
        #     tags_dict[tag["tag_id"]] = tag_model
        return {}
        # return list(tags_dict.values())

    def get_tag_list_from_streams(self, streams):
        tag_ids = []
        try:
            for s in streams["data"]:
                for tag in s["tag_ids"]:
                    tag_ids.append(tag)
        except Exception as e:
            print(e)
        return tag_ids
