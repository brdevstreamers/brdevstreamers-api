from github import Github
from dotenv import dotenv_values

config = dotenv_values(".env")

def has_github_account(username):
    try:
        g = Github(config["GITHUB_TOKEN"])
        user = g.get_user(username)
        return True
    except:
        return False