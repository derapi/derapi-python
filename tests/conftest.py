import os

import httpx
import pytest

from derapi import AuthenticatedClient


@pytest.fixture(scope="session")
def client():
    token = _request_token(
        os.environ["DERAPI_TOKEN_URL"],
        os.environ["DERAPI_CLIENT_ID"],
        os.environ["DERAPI_CLIENT_SECRET"],
    )
    return AuthenticatedClient(
        os.environ["DERAPI_URL"],
        headers={"api-version": "v2024-09-01"},
        raise_on_unexpected_status=True,
        token=token,
    )


@pytest.fixture(scope="session")
def virtual_client():
    token = _request_token(
        os.environ["DERAPI_TOKEN_URL"],
        os.environ["DERAPI_VIRTUAL_CLIENT_ID"],
        os.environ["DERAPI_VIRTUAL_CLIENT_SECRET"],
    )
    client = AuthenticatedClient(
        os.environ["DERAPI_URL"],
        headers={"api-version": "v2024-09-01"},
        raise_on_unexpected_status=True,
        token=token,
    )

    def log_request(r: httpx.Request):
        print(f"Request: {r.method} {r.url} {r.headers}")

    client.get_httpx_client().event_hooks["request"].append(log_request)
    return client


def _request_token(token_url: str, client_id: str, client_secret: str) -> str:
    resp = httpx.post(
        token_url,
        auth=(client_id, client_secret),
        data={"grant_type": "client_credentials"},
    )
    resp.raise_for_status()
    return resp.json()["access_token"]
