from core import settings
from github import Github

user_githubs = {}


def has_github_account(username):
    try:
        if username not in user_githubs:
            g = Github(settings.GITHUB_TOKEN)
            user = g.get_user(username)
            user_githubs[username] = True
    except:
        user_githubs[username] = False

    return user_githubs[username]