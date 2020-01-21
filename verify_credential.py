from connect import connect_agents
import requests
import urllib
from config import client_url


def verify_credential(base_url, connection_id):
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
    requests.post(url, json=content)


def main():
    connection_id = connect_agents()
    verify_credential(client_url, connection_id)


if __name__ == '__main__':
    main()
