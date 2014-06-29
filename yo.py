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

class Yo(object):
    """A Yo user."""
    def __init__(self):
        super(Yo, self).__init__()
    def login(self, username, password):
        #TODO: this
        pass
    def make(self, username, password):
        #TODO: this
        pass
    def yo(self, recipient, repetitions=1):
        recipient = recipient.upper() # Yo doesn't do lowercase.
        payload = {
            'data': {'to':recipient},
            'session_token': self.session_token,
            'function': 'yo'
        }
        for i in xrange(repetitions):
            r = requests.post(url, data=json.dumps(payload), headers=self.headers)
            print(r.text)
    def check(self, sender):
        #TODO: this
        # Returns the Firebase value and sets it to False.
        return False
    def headers(self):
        return {
            'Authorization': authorization,
            'content-type': 'application/json'
        }
        
    authorization = ''
    session_token = ''
    