from twitter import *
from dotenv import dotenv_values

config = dotenv_values(".env")
t = Twitter(
    auth=OAuth(
        config['TWITTER_ACCESS_TOKEN'], 
        config['TWITTER_ACCESS_SECRET'],
        config['TWITTER_API_KEY'], 
        config['TWITTER_API_SECRET']))

def has_twitter_account(username):
    try:
        users = t.users.lookup(screen_name=username, _timeout=1)
        return len(users) > 0
    except:
        return False

def get_twitter_accounts(usernames):
    # try:
    users = t.users.lookup(screen_name=','.join(usernames), _timeout=1)
    user_names = []
    for user in users:
        user_names.append(user['screen_name'].lower())
    return user_names
    # except:
    #     return False