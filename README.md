This is a demo script for the Universal Resolver DIDComm agent interface (see https://github.com/danubetech/universal-resolver-didcomm).

# Overview

The demo script will invoke a client DIDComm agent, which will in turn open a connection to a Universal Resolver DIDComm agent for a DID resolution request.

The demo script requires a DIDComm connection invitation generated by the Universal Resolver DIDComm agent.

The demo script is marked in red in the following diagram:

![architecture-demo-script](https://raw.githubusercontent.com/danubetech/universal-resolver-didcomm-demo/main/diagrams/architecture-demo-script.png)

# Run the demo script

First, make sure that you have both a client DIDComm agent and a Universal Resolver DIDComm agent you can use for the demo script (see https://github.com/hyperledger/aries-cloudagent-python/).

Run `resolve_did.py` to connect the client DIDComm agent to the Universal Resolver DIDComm agent, and then instruct the client DIDComm agent to send a DID resolution request.

```
python3 resolve_did.py --invitation-path=~/didcomm-invitation.txt
# alternatively, use the base64 encoded invitation directly:
python3 resolve_did.py --invitation=eyJAdHlw...
```

In the log of the Universal Resolver DIDComm agent you should see the DID resolution request arriving,
and on the client DIDComm agent you should then see the resolved DID document from the DIDComm
message.

