from twitchAPI.twitch import Twitch

from core import settings

twitch = Twitch(settings.CLIENT_ID, settings.CLIENT_SECRET)

users = twitch.get_users(user_ids=['227168488'])


print(users)
