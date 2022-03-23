
import requests

        

def get_contributors():
    r_server = requests.get('https://api.github.com/repos/Br-Dev-Streamers/brdevstreamers/contributors')
    contrib_server = r_server.json()

    r_ui = requests.get('https://api.github.com/repos/Br-Dev-Streamers/brdevstreamers-ui/contributors')
    contrib_ui = r_ui.json()

    contributors_list = []

    for c in contrib_server:
        contributor = {"name": c['login'], "image": c["avatar_url"]}
        contributors_list.append(contributor)
    
    for c in contrib_ui:
        if not_in_list(contributors_list, c['login']):
            contributor = {"name": c['login'], "image": c["avatar_url"]}
            contributors_list.append(contributor)

    return contributors_list

def not_in_list(list, login):
    for contributor in list:
        if contributor['name'] == login:
            return False
    return True