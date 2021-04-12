# Purpose

This is a test script for the Universal Resolver DIDComm agent interface (see https://github.com/danubetech/universal-resolver-didcomm).

The test script will invoke a client DIDComm agent, which will in turn open a connection to a Universal Resolver DIDComm agent for a DID resolution request.

# Components

The component marked in red is provided by this repository.

![architecture-test-script](https://raw.githubusercontent.com/danubetech/universal-resolver-didcomm-demo/main/diagrams/architecture-test-script.png)

# Run the demo

First, deploy the client agent 

Finally run `resolve_did.py` to connect the client DIDComm agent to the Universal Resolver DIDComm agent, and then instruct the client DIDComm agent to send a DID resolution request.

```
python3 resolve_did.py --invitation-path=~/didcomm-invitation.txt
# alternatively, use the base64 encoded invitation directly:
python3 resolve_did.py --invitation=eyJAdHlw...
```

In the log of the Universal Resolver DIDComm agent you should see the DID resolution request arriving,
and on the client DIDComm agent you should then see the resolved DID document from the DIDComm
message.

