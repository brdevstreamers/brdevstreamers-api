from twitchAPI.twitch import Twitch
from dotenv import dotenv_values
config = dotenv_values(".env")


twitch = Twitch(config['CLIENT_ID'], config['CLIENT_SECRET'])

games = twitch.get_games(names=['Software and Game Development'])

game_id = games['data'][0]['id']

streams = twitch.get_streams(language="pt", game_id=game_id)

for stream in streams['data']:
    if stream['game_id'] == game_id:
        print(stream['user_login'])
