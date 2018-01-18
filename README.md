# PyHive
Python class for interfacing with CoinHive's HTTP API.


# Example (GET)
```py
from pyhive import PyHiveClient

secret_key = ""
client = PyHiveClient(secret_key)

client.get("/stats/site")
```

# Example (POST)
```py
from pyhive import PyHiveClient


secret_key = ""
client = PyHiveClient(secret_key)

client.post("/links/create", {"url": "https://example.com", "hashes": 1024})
```
