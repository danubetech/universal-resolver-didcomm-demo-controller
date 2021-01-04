import click
from connect import connect_agents
import requests
from config import client_url
import urllib


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
    requests.post(url, json=content)


@click.command()
@click.option('--invitation-path', default=None,
              help='path of the invitation file.')
@click.option('--invitation', default=None, help='base64-encoded invitation.')
def main(invitation_path, invitation):
    connection_id = connect_agents(invitation_path=invitation_path,
                                   invitation=invitation)
    resolve_did(client_url, connection_id)


if __name__ == '__main__':
    main()
