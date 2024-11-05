from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_vendor_credentials_response import GetVendorCredentialsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    include_secrets: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["includeSecrets"] = include_secrets

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/vendor-credentials/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetVendorCredentialsResponse]:
    if response.status_code == 200:
        response_200 = GetVendorCredentialsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetVendorCredentialsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include_secrets: Union[Unset, bool] = False,
) -> Response[GetVendorCredentialsResponse]:
    """Fetches specified credentials

     Fetches the Derapi managed credentials for the specified vendor and name

    Args:
        id (str): ID for the vendor credentials
        include_secrets (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVendorCredentialsResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        include_secrets=include_secrets,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include_secrets: Union[Unset, bool] = False,
) -> Optional[GetVendorCredentialsResponse]:
    """Fetches specified credentials

     Fetches the Derapi managed credentials for the specified vendor and name

    Args:
        id (str): ID for the vendor credentials
        include_secrets (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVendorCredentialsResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        include_secrets=include_secrets,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include_secrets: Union[Unset, bool] = False,
) -> Response[GetVendorCredentialsResponse]:
    """Fetches specified credentials

     Fetches the Derapi managed credentials for the specified vendor and name

    Args:
        id (str): ID for the vendor credentials
        include_secrets (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVendorCredentialsResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        include_secrets=include_secrets,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include_secrets: Union[Unset, bool] = False,
) -> Optional[GetVendorCredentialsResponse]:
    """Fetches specified credentials

     Fetches the Derapi managed credentials for the specified vendor and name

    Args:
        id (str): ID for the vendor credentials
        include_secrets (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVendorCredentialsResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            include_secrets=include_secrets,
        )
    ).parsed
