from twitchAPI.twitch import Twitch
from dotenv import dotenv_values
config = dotenv_values(".env")


twitch = Twitch(config['CLIENT_ID'], config['CLIENT_SECRET'])

users = twitch.get_users(user_ids=['227168488'])


print(users)
