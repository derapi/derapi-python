# derapi

The `derapi` Python SDK provides access to the Derapi API for Python
applications -- fully typed with async support.

[![PyPI - Version](https://img.shields.io/pypi/v/derapi.svg)](https://pypi.org/project/derapi)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/derapi.svg)](https://pypi.org/project/derapi)

-----

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

```shell
pip install derapi
```

## Usage

Client initialization:

```python
import os

import httpx
from derapi import AuthenticatedClient

def init_client() -> AuthenticatedClient:
    token_resp = httpx.post(
        "https://auth.derapi.com/oauth2/token",
        auth=(os.environ["DERAPI_CLIENT_ID"], os.environ["DERAPI_CLIENT_SECRET"]),
        data={"grant_type": "client_credentials"},
    )
    token_resp.raise_for_status()
    token = token_resp.json()["access_token"]
    return AuthenticatedClient(
        base_url="https//api.derapi.com",
        raise_on_unexpected_status=True,
        token=token,
    )
```

Usage:

```python
...

from derapi.api import list_sites

client = init_client()

for site in list_sites.sync_depaginated(client=client):
    print(site.id)
```

## License

`derapi` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
