from twitchAPI.twitch import Twitch
from dotenv import dotenv_values
from service.github_service import has_github_account

from service.twitter_service import get_twitter_accounts, has_twitter_account

config = dotenv_values(".env")
twitch = Twitch(config['CLIENT_ID'], config['CLIENT_SECRET'])

def get_streamers():

    games = twitch.get_games(names=['Software and Game Development'])
    game_id = games['data'][0]['id']
    streams = twitch.get_streams(language="pt", game_id=game_id)

    user_logins = []

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
        stream['description'] = streamer['description']
        
        stream['has_github'] = has_github_account(s['user_login'])
        streams_model.append(stream)
        user_logins.append(s['user_login'])

    twitter_accounts = get_twitter_accounts(user_logins)
    for model in streams_model:
        model['has_twitter'] = model['user_login'].lower() in twitter_accounts

            

    return streams_model

def get_streamer(id):
    return twitch.get_users(user_ids=[id])['data'][0]
    
