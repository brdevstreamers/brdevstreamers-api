from core import settings
from twitter import *

t = Twitter(
    auth=OAuth(
        settings.TWITTER_ACCESS_TOKEN,
        settings.TWITTER_ACCESS_SECRET,
        settings.TWITTER_API_KEY,
        settings.TWITTER_API_SECRET,
    )
)

user_twitters = {}

def has_twitter_account(username):
    try:
        if username not in user_twitters:
            users = t.users.lookup(screen_name=username, _timeout=1)
            user_twitters[username] = len(users) > 0
    except:
        user_twitters[username] = False
        
    return user_twitters[username]
