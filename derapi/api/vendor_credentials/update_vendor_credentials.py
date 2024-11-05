from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_vendor_credentials_request import UpdateVendorCredentialsRequest
from ...models.update_vendor_credentials_response import UpdateVendorCredentialsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: Union[
        UpdateVendorCredentialsRequest,
        UpdateVendorCredentialsRequest,
    ],
    include_secrets: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["includeSecrets"] = include_secrets

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/vendor-credentials/{id}",
        "params": params,
    }

    if isinstance(body, UpdateVendorCredentialsRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/merge-patch+json"
    if isinstance(body, UpdateVendorCredentialsRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UpdateVendorCredentialsResponse]:
    if response.status_code == 200:
        response_200 = UpdateVendorCredentialsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UpdateVendorCredentialsResponse]:
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
    body: Union[
        UpdateVendorCredentialsRequest,
        UpdateVendorCredentialsRequest,
    ],
    include_secrets: Union[Unset, bool] = False,
) -> Response[UpdateVendorCredentialsResponse]:
    """Updates the stored credentials

     Updates the stored credentials with the given ID. The request body will be interpreted as a [JSON
    Merge Patch](https://datatracker.ietf.org/doc/html/rfc7396) against the stored credentials.  Note
    that updating the 'vendor' or 'type' fields is not supported.

    Args:
        id (str): ID for the vendor credentials
        include_secrets (Union[Unset, bool]):  Default: False.
        body (UpdateVendorCredentialsRequest):
        body (UpdateVendorCredentialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateVendorCredentialsResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
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
    body: Union[
        UpdateVendorCredentialsRequest,
        UpdateVendorCredentialsRequest,
    ],
    include_secrets: Union[Unset, bool] = False,
) -> Optional[UpdateVendorCredentialsResponse]:
    """Updates the stored credentials

     Updates the stored credentials with the given ID. The request body will be interpreted as a [JSON
    Merge Patch](https://datatracker.ietf.org/doc/html/rfc7396) against the stored credentials.  Note
    that updating the 'vendor' or 'type' fields is not supported.

    Args:
        id (str): ID for the vendor credentials
        include_secrets (Union[Unset, bool]):  Default: False.
        body (UpdateVendorCredentialsRequest):
        body (UpdateVendorCredentialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateVendorCredentialsResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        include_secrets=include_secrets,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        UpdateVendorCredentialsRequest,
        UpdateVendorCredentialsRequest,
    ],
    include_secrets: Union[Unset, bool] = False,
) -> Response[UpdateVendorCredentialsResponse]:
    """Updates the stored credentials

     Updates the stored credentials with the given ID. The request body will be interpreted as a [JSON
    Merge Patch](https://datatracker.ietf.org/doc/html/rfc7396) against the stored credentials.  Note
    that updating the 'vendor' or 'type' fields is not supported.

    Args:
        id (str): ID for the vendor credentials
        include_secrets (Union[Unset, bool]):  Default: False.
        body (UpdateVendorCredentialsRequest):
        body (UpdateVendorCredentialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateVendorCredentialsResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        include_secrets=include_secrets,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        UpdateVendorCredentialsRequest,
        UpdateVendorCredentialsRequest,
    ],
    include_secrets: Union[Unset, bool] = False,
) -> Optional[UpdateVendorCredentialsResponse]:
    """Updates the stored credentials

     Updates the stored credentials with the given ID. The request body will be interpreted as a [JSON
    Merge Patch](https://datatracker.ietf.org/doc/html/rfc7396) against the stored credentials.  Note
    that updating the 'vendor' or 'type' fields is not supported.

    Args:
        id (str): ID for the vendor credentials
        include_secrets (Union[Unset, bool]):  Default: False.
        body (UpdateVendorCredentialsRequest):
        body (UpdateVendorCredentialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateVendorCredentialsResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            include_secrets=include_secrets,
        )
    ).parsed
