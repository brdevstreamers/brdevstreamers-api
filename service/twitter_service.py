from twitter import *
from dotenv import dotenv_values

config = dotenv_values(".env")
t = Twitter(
    auth=OAuth(
        config['TWITTER_ACCESS_TOKEN'], 
        config['TWITTER_ACCESS_SECRET'],
        config['TWITTER_API_KEY'], 
        config['TWITTER_API_SECRET']))

user_twitters = {}

def has_twitter_account(username):
    try:
        if username not in user_twitters:
            users = t.users.lookup(screen_name=username, _timeout=1)
            user_twitters[username] = len(users) > 0
    except:
        user_twitters[username] = False
        
    return user_twitters[username]
