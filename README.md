# Purpose

This is a demo for aries-cloudagent-python.
It connects two agents via didcomm, and then sends a did resolution request
from one agent to the other agent. For the DID resolution
https://uniresolver.io is used.

# Run the demo

For a basic (insecure) demo on localhost:
```
# install aries-cloudagent including the did resolution protocol
mkdir venv
virtualenv -p python3.7 venv/
source venv/bin/activate
git clone https://gitlab.com/ffon/aries-cloudagent-python
cd aries-cloudagent-python
git checkout did-resolution
pip install --no-cache-dir -e .
```

Then start two agents, acting as a server and a client (in a separate shell after activating the virtualenv again):
```
# server
aca-py start --admin-insecure-mode --admin 127.0.0.1 3000 -it http 127.0.0.1 3555 -ot http --auto-accept-invites --auto-accept-requests --endpoint http://127.0.0.1:3555 --auto-respond-messages --label Server --auto-ping-connection --log-level debug
# docker server (image built with aries-cloudagent-container)
docker run --net=host -p 3000:3000 -p 3555:3555 -i -t 4bae9e775869 start --admin-insecure-mode --admin 0.0.0.0 3000 -it http 0.0.0.0 3555 -ot http --auto-accept-invites -- auto-accept-requests --endpoint http://0.0.0.0:3555 --auto-respond-messages --label Server --auto-ping-connection --log-level debug

# client (will execute the didcomm queries)
aca-py start --admin-insecure-mode --admin 127.0.0.1 4000 -it http 127.0.0.1 4555 -ot http --auto-accept-invites --auto-accept-requests --endpoint http://127.0.0.1:4555 --auto-store-credential --auto-respond-messages --label Client --auto-ping-connection --log-level debug
# docker client
docker run --net=host -p 4000:4000 -p 4555:4555 -i -
t 4bae9e775869 start --admin-insecure-mode --admin 0.0.0.0 4000 -it http 0.0.0.0 4555 -ot http --auto-accept-invites --aut
o-accept-requests --endpoint http://0.0.0.0:4555 --auto-store-credential --auto-respond-messages --label Client --auto-pin
g-connection --log-level debug
```

Finally run `resolve_did.py` to connect the agents, and tell the client to
send a did resolution request to the server:

```
python3 resolve_did.py
```

In the log of the server you should see the did resolution request arriving,
and on the client you should then see the resolved did document of the didcomm
message.
