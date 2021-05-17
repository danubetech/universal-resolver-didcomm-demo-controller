import click
from connect import connect_agents
import requests
from config import client_url
import urllib


def resolve_did(base_url, connection_id):
    did = "did:sov:WRfXPg8dantKVubE3HX8pw"
    url = urllib.parse.urljoin(base_url,
                               f"connections/{connection_id}/resolve-did")
    # url = urllib.parse.urljoin(base_url,
    #                            f"resolver/resolve-did/{did}")
    content = {
        "@type": "https://didcomm.org/did_resolution/0.1",
        "@id": "xhqMoTXfqhvAgtYxUSfaxbSiqWke9t",
        "did": did,
        "input_options": {
            "result_type": "did-document",
            "no_cache": False
        },
        "content": ""
    }
    response = requests.post(url, json=content)
    print(response)


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
