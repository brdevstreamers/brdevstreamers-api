
import requests

        

def get_contributors():
    r_server = requests.get('https://api.github.com/repos/Br-Dev-Streamers/brdevstreamers/contributors')
    contrib_server = r_server.json()

    r_ui = requests.get('https://api.github.com/repos/Br-Dev-Streamers/brdevstreamers-ui/contributors')
    contrib_ui = r_ui.json()

    contributors_dict = {}
    
    for c in contrib_server:
        contributors_dict[c['login']] = c["avatar_url"]
    
    for c in contrib_ui:
        contributors_dict[c['login']] = c["avatar_url"]
    return contributors_dict.items()

