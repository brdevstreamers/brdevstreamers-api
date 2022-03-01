from random import shuffle
from twitchAPI.twitch import Twitch
from dotenv import dotenv_values
from model.user_model import User
from service.github_service import has_github_account
from twitchAPI.types import TimePeriod
from service.twitter_service import has_twitter_account
from typing import List
from view_model.stream_viewmodel import StreamViewModel
from view_model.vod_viewmodel import VodViewModel
from view_model.tag_viewmodel import TagViewModel

config = dotenv_values(".env")
twitch = Twitch(config['CLIENT_ID'], config['CLIENT_SECRET'])


def get_streamers() -> List[StreamViewModel]:
    streams = twitch.get_streams(language="pt", game_id='1469308723')

    streams_model: List[StreamViewModel] = []
    stream_users = []
    for s in streams['data']:
        stream = StreamViewModel()
        stream.id = s['id']
        stream.user_id = s['user_id']
        stream.user_name = s['user_name']
        stream.user_login = s['user_login']
        stream.title = s['title']
        stream.viewer_count = s['viewer_count']
        stream.started_at = s['started_at']
        stream.thumbnail_url = s['thumbnail_url']

        stream.tags = s['tag_ids'] 

        streamer = get_streamer(s['user_id'])
        stream.profile_image_url = streamer['profile_image_url']
        stream.description = streamer['description'][:100] + '...'

        stream_users.append(s['user_login'])
        streams_model.append(stream)

    streamers = User.select().where(User.user_login << stream_users).execute()
    for s in streamers:
        for stream in streams_model:
            if(stream.user_login == s.user_login):
                stream.github_url = s.github
                stream.twitter_url = s.twitter
                stream.instagram_url = s.instagram
                stream.linkedin_url = s.linkedin
                stream.discord_url = s.discord
                stream.bio = s.bio
                break
    shuffle(streams_model)
    return streams_model


def get_streamer(id):
    return twitch.get_users(user_ids=[id])['data'][0]


def get_vods() -> List[VodViewModel]:
    vods = twitch.get_videos(
        language="pt", game_id='1469308723', period=TimePeriod.DAY)
    vods_model: List[VodViewModel] = []
    vod_users = []

    for s in vods['data']:
        if is_long_enough(s['duration']):
            stream = VodViewModel()
            stream.id = s['id']
            stream.user_id = s['user_id']
            stream.user_name = s['user_name']
            stream.user_login = s['user_login']
            stream.title = s['title']
            stream.viewer_count = s['view_count']
            stream.started_at = s['published_at']
            stream.thumbnail_url = s['thumbnail_url']
            stream.stream_id = s['id']
            stream.duration = s['duration']

            streamer = get_streamer(s['user_id'])
            stream.profile_image_url = streamer['profile_image_url']
            stream.description = streamer['description'][:100] + '...'

            vod_users.append(s['user_login'])
            vods_model.append(stream)

    streamers = User.select().where(User.user_login << vod_users).execute()
    for s in streamers:
        for stream in vods_model:
            if(stream.user_login == s.user_login):
                stream.github_url = s.github
                stream.twitter_url = s.twitter
                stream.instagram_url = s.instagram
                stream.linkedin_url = s.linkedin
                stream.discord_url = s.discord
                stream.bio = s.bio
                break

    return vods_model


def is_long_enough(duration):
    return 'h' in duration


def get_tags() -> List[TagViewModel]:
    streams = twitch.get_streams(language="pt", game_id='1469308723')
    tag_ids = get_tag_list_from_streams(streams)
    tags = twitch.get_all_stream_tags(tag_ids=tag_ids)
    tags_list = []
    for tag in tags['data']:
        tag_model = TagViewModel(
            id=tag['tag_id'], name=tag['localization_names']['pt-br'])
        tags_list.append(tag_model)
    return tags_list


def get_tag_list_from_streams(streams):
    tag_ids = []
    for s in streams['data']:
        for tag in s['tag_ids']:
            tag_ids.append(tag)
    return tag_ids

