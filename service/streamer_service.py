from twitchAPI.twitch import Twitch
from dotenv import dotenv_values
from model.streamer_model import Streamer
from service.github_service import has_github_account
from twitchAPI.types import TimePeriod
from service.twitter_service import has_twitter_account

config = dotenv_values(".env")
twitch = Twitch(config['CLIENT_ID'], config['CLIENT_SECRET'])

def get_streamers():
    games = twitch.get_games(names=['Software and Game Development'])
    game_id = games['data'][0]['id']
    streams = twitch.get_streams(language="pt", game_id=game_id)
 
    streams_model = []
    for s in streams['data']:
        stream = {}
        stream['id'] = s['id']
        stream['user_id'] = s['user_id']
        stream['user_name'] = s['user_name']
        stream['user_login'] = s['user_login']
        stream['title'] = s['title']
        stream['viewer_count'] = s['viewer_count']
        stream['started_at'] = s['started_at']
        stream['thumbnail_url'] = s['thumbnail_url']

        streamer = get_streamer(s['user_id'])
        stream['profile_image_url'] = streamer['profile_image_url']
        stream['description'] = streamer['description'][:100] + '...'

        try:
            streamer_model = Streamer.select().where(Streamer.user_login == s['user_login']).get()
            stream['github_url'] = streamer_model.github
            stream['twitter_url'] = streamer_model.twitter
            stream['instagram_url'] = streamer_model.instagram
            stream['linkedin_url'] = streamer_model.linkedin
            stream['discord_url'] = streamer_model.discord
        except:
            print('User Not Found')
        finally:
            streams_model.append(stream)

    return streams_model

def get_streamer(id):
    return twitch.get_users(user_ids=[id])['data'][0]
    

def get_vods():
    games = twitch.get_games(names=['Software and Game Development'])
    game_id = games['data'][0]['id']
    vods = twitch.get_videos(language="pt", game_id=game_id, period=TimePeriod.DAY)
    vods_model = []
    for s in vods['data']:
        if is_long_enough(s['duration']):
            stream = {}
            stream['id'] = s['id']
            stream['user_id'] = s['user_id']
            stream['user_name'] = s['user_name']
            stream['user_login'] = s['user_login']
            stream['title'] = s['title']
            stream['viewer_count'] = s['view_count']
            stream['started_at'] = s['published_at']
            stream['thumbnail_url'] = s['thumbnail_url']
            stream['stream_id'] = s['id']
            stream['duration'] = s['duration']
            streamer = get_streamer(s['user_id'])
            stream['profile_image_url'] = streamer['profile_image_url']
            stream['description'] = streamer['description'][:100] + '...'

            try:
                streamer_model = Streamer.select().where(Streamer.user_login == s['user_login']).get()
                stream['github_url'] = streamer_model.github
                stream['twitter_url'] = streamer_model.twitter
                stream['instagram_url'] = streamer_model.instagram
                stream['linkedin_url'] = streamer_model.linkedin
                stream['discord_url'] = streamer_model.discord
            except:
                print('User Not Found')
            finally:
                vods_model.append(stream)

    return vods_model


def is_long_enough(duration):
    return 'h' in duration
    

