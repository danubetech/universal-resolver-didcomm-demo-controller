"""
Establish a connection between two cloud agents, using their REST APIs
"""

import requests
import urllib
import json


agent1 = "http://127.0.0.1:3000"
agent2 = "http://127.0.0.1:4000"

"""
These agents can be started like:
    agent1:
        aca-py start --admin-insecure-mode --admin 127.0.0.1 3000 -it http
        127.0.0.1 3555 -ot http --auto-accept-invites --auto-accept-requests
        --endpoint http://127.0.0.1:3555 --auto-respond-messages --label Faber
        --auto-ping-connection
    agent2:
        aca-py start --admin-insecure-mode --admin 127.0.0.1 4000 -it http
        127.0.0.1 4555 -ot http --auto-accept-invites --auto-accept-requests
        --endpoint http://127.0.0.1:4555 --auto-store-credential
        --auto-respond-messages --label Alice --auto-ping-connection
"""

session = requests.Session()
session.headers.update({'Accept': 'application/json'})


def create_invitation(base_url):
    url = urllib.parse.urljoin(base_url, 'connections/create-invitation')
    return session.post(url).json()


def receive_invitation(base_url, invitation):
    url = urllib.parse.urljoin(base_url, 'connections/receive-invitation')
    return session.post(url, json=invitation)


def connect_agents():
    invite_response = create_invitation(agent1)
    response = receive_invitation(agent2, invite_response['invitation'])
    assert(response.status_code == 200)


if __name__ == '__main__':
    connect_agents()
