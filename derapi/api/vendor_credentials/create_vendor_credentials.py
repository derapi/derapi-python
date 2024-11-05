from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_vendor_credentials_request import CreateVendorCredentialsRequest
from ...models.create_vendor_credentials_response import CreateVendorCredentialsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateVendorCredentialsRequest,
    include_secrets: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["includeSecrets"] = include_secrets

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/vendor-credentials",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CreateVendorCredentialsResponse]:
    if response.status_code == 201:
        response_201 = CreateVendorCredentialsResponse.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CreateVendorCredentialsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateVendorCredentialsRequest,
    include_secrets: Union[Unset, bool] = False,
) -> Response[CreateVendorCredentialsResponse]:
    """Stores vendor credentials

     Stores vendor credentials as specified.

    Args:
        include_secrets (Union[Unset, bool]):  Default: False.
        body (CreateVendorCredentialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateVendorCredentialsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        include_secrets=include_secrets,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateVendorCredentialsRequest,
    include_secrets: Union[Unset, bool] = False,
) -> Optional[CreateVendorCredentialsResponse]:
    """Stores vendor credentials

     Stores vendor credentials as specified.

    Args:
        include_secrets (Union[Unset, bool]):  Default: False.
        body (CreateVendorCredentialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateVendorCredentialsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        include_secrets=include_secrets,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateVendorCredentialsRequest,
    include_secrets: Union[Unset, bool] = False,
) -> Response[CreateVendorCredentialsResponse]:
    """Stores vendor credentials

     Stores vendor credentials as specified.

    Args:
        include_secrets (Union[Unset, bool]):  Default: False.
        body (CreateVendorCredentialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateVendorCredentialsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        include_secrets=include_secrets,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateVendorCredentialsRequest,
    include_secrets: Union[Unset, bool] = False,
) -> Optional[CreateVendorCredentialsResponse]:
    """Stores vendor credentials

     Stores vendor credentials as specified.

    Args:
        include_secrets (Union[Unset, bool]):  Default: False.
        body (CreateVendorCredentialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateVendorCredentialsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            include_secrets=include_secrets,
        )
    ).parsed
