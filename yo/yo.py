# USAGE:
# import yo.yo as yo

import os
import json
import requests


url = 'https://api.parse.com/2/client_function'

headers = {
    'Authorization': os.environ['YO_AUTHORIZATION'],
    'content-type': 'application/json'
}

session_token = os.environ['YO_SESSION_TOKEN']


def yo(u, n=1):
    u = u.upper() # Yo doesn't do lowercase.
    payload = {
        "data": { "to": u },
        "session_token": session_token,
        "function": "yo"
    }
    for i in xrange(n):
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        print(r.text)
    return

