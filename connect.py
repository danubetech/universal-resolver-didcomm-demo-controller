"""
Establish a connection between two cloud agents, using their REST APIs
"""

import base64
from config import client_url
from errors import NotConnectedError
import json
import os

import requests
import time
import urllib

session = requests.Session()
session.headers.update({'Accept': 'application/json'})


"""
These agents can be started like:
    server:
        aca-py start -it http 127.0.0.1 3555 -ot http --auto-accept-invites
        --auto-accept-requests --endpoint http://127.0.0.1:3555
        --auto-respond-messages --label Server --log-level debug
        --public-invite --invite --invite-base-url http://localhost:3555
        --invite-multi-use --no-ledger --admin-insecure-mode --admin 127.0.0.1
        3000 --write-invitation-to=/home/username/.invitation.txt
    client:
        aca-py start --admin-insecure-mode --admin 127.0.0.1 4000 -it http 127.0.0.1 4555 -ot http --auto-accept-invites --auto-accept-requests --endpoint http://127.0.0.1:4555 --auto-store-credential --auto-respond-messages --label Client --auto-ping-connection --log-level debug --no-ledger
"""


def create_invitation(base_url):
    url = urllib.parse.urljoin(base_url, 'connections/create-invitation')
    return session.post(url).json()


def receive_invitation(base_url, invitation):
    url = urllib.parse.urljoin(base_url, 'connections/receive-invitation')
    return session.post(url, json=invitation)


def receive_invitation_didexchange(base_url, invitation):
    url = urllib.parse.urljoin(base_url, 'didexchange/receive-invitation')
    return session.post(url, json=invitation)


def get_connection_id(base_url):
    """Get an active connection id"""
    url = urllib.parse.urljoin(base_url, 'connections')
    response = session.get(url)
    if response.ok:
        connections = response.json()
        active_ids = [result['connection_id'] for result in
                      connections['results'] if result['state'] == 'active']
        if active_ids:
            return active_ids[0]

    raise NotConnectedError()


def _connect_agents(invitation_path, invitation):
    if invitation_path == invitation:
        raise ValueError('Provide either invitation_path or the invitation')

    if invitation_path is not None:
        expanded_path = os.path.expanduser(invitation_path)
        with open(expanded_path) as handle:
            invitation = handle.readline().strip()

    # if the invitation is not valid json try base64 decoding it first
    try:
        invitation = json.loads(invitation)
    except json.decoder.JSONDecodeError:
        invitation = base64.b64decode(invitation).decode()
        invitation = json.loads(invitation)
        print(f"decoded invitation: \n{invitation}")

    print('receive invitation, body: ')
    print(invitation)
    response = receive_invitation_didexchange(client_url, invitation)
    assert(response.status_code == 200)


def connect_agents(invitation_path, invitation):
    try:
        connection_id = get_connection_id(client_url)
    except NotConnectedError:
        _connect_agents(invitation_path, invitation)
        # TODO: wait until connection shows up in /connections
        time.sleep(1.5)
        connection_id = get_connection_id(client_url)
    return connection_id


if __name__ == '__main__':
    connect_agents()
