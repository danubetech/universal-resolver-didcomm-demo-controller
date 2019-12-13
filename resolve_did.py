from connect import connect_agents
import requests
from errors import NotConnectedError
import urllib
import time

agent1 = "http://127.0.0.1:3000"
agent2 = "http://127.0.0.1:4000"

session = requests.Session()
session.headers.update({'Accept': 'application/json'})


def resolve_did(base_url, connection_id):
    url = urllib.parse.urljoin(base_url,
                               f"connections/{connection_id}/resolve-did")
    content = {
        "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/did_resolution/0.1/resolve",
        "@id": "xhqMoTXfqhvAgtYxUSfaxbSiqWke9t",
        "did": "did:sov:WRfXPg8dantKVubE3HX8pw",
        "input_options": {
            "result_type": "did-document",
            "no_cache": False
        },
        "content": ""
    }
    response = requests.post(url, json=content)


def get_connection_id(base_url):
    """Get an active connection id"""
    url = urllib.parse.urljoin(base_url, 'connections')
    response = session.get(url)
    if response.ok:
        connections = response.json()
        active_ids =  [result['connection_id'] for result in
                       connections['results'] if result['state'] == 'active']
        if active_ids:
            return active_ids[0]

    raise NotConnectedError()


def main():
    try:
        connection_id = get_connection_id(agent2)
    except NotConnectedError:
        connect_agents()
        # TODO: wait until connection shows up in /connections
        time.sleep(0.5)
        connection_id = get_connection_id(agent2)

    resolve_did(agent2, connection_id)


if __name__ == '__main__':
    main()
