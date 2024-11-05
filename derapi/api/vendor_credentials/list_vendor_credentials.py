from http import HTTPStatus
from typing import Any, AsyncIterator, Dict, Iterator, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_vendor_credentials_response import ListVendorCredentialsResponse
from ...models.vendor import Vendor
from ...models.vendor_credentials import VendorCredentials
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
    vendor: Union[Unset, Vendor] = UNSET,
    name: Union[Unset, str] = UNSET,
    include_secrets: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    json_vendor: Union[Unset, str] = UNSET
    if not isinstance(vendor, Unset):
        json_vendor = vendor.value

    params["vendor"] = json_vendor

    params["name"] = name

    params["includeSecrets"] = include_secrets

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/vendor-credentials",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListVendorCredentialsResponse]:
    if response.status_code == 200:
        response_200 = ListVendorCredentialsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListVendorCredentialsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
    vendor: Union[Unset, Vendor] = UNSET,
    name: Union[Unset, str] = UNSET,
    include_secrets: Union[Unset, bool] = False,
) -> Response[ListVendorCredentialsResponse]:
    """Lists stored vendor credentials

     Lists stored vendor credentials, paginated and optionally filtered.

    Args:
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):
        vendor (Union[Unset, Vendor]):
        name (Union[Unset, str]):
        include_secrets (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListVendorCredentialsResponse]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page_token=page_token,
        vendor=vendor,
        name=name,
        include_secrets=include_secrets,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
    vendor: Union[Unset, Vendor] = UNSET,
    name: Union[Unset, str] = UNSET,
    include_secrets: Union[Unset, bool] = False,
) -> Optional[ListVendorCredentialsResponse]:
    """Lists stored vendor credentials

     Lists stored vendor credentials, paginated and optionally filtered.

    Args:
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):
        vendor (Union[Unset, Vendor]):
        name (Union[Unset, str]):
        include_secrets (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListVendorCredentialsResponse
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        page_token=page_token,
        vendor=vendor,
        name=name,
        include_secrets=include_secrets,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
    vendor: Union[Unset, Vendor] = UNSET,
    name: Union[Unset, str] = UNSET,
    include_secrets: Union[Unset, bool] = False,
) -> Response[ListVendorCredentialsResponse]:
    """Lists stored vendor credentials

     Lists stored vendor credentials, paginated and optionally filtered.

    Args:
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):
        vendor (Union[Unset, Vendor]):
        name (Union[Unset, str]):
        include_secrets (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListVendorCredentialsResponse]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page_token=page_token,
        vendor=vendor,
        name=name,
        include_secrets=include_secrets,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
    vendor: Union[Unset, Vendor] = UNSET,
    name: Union[Unset, str] = UNSET,
    include_secrets: Union[Unset, bool] = False,
) -> Optional[ListVendorCredentialsResponse]:
    """Lists stored vendor credentials

     Lists stored vendor credentials, paginated and optionally filtered.

    Args:
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):
        vendor (Union[Unset, Vendor]):
        name (Union[Unset, str]):
        include_secrets (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListVendorCredentialsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            page_token=page_token,
            vendor=vendor,
            name=name,
            include_secrets=include_secrets,
        )
    ).parsed


def sync_depaginated(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
    vendor: Union[Unset, Vendor] = UNSET,
    name: Union[Unset, str] = UNSET,
    include_secrets: Union[Unset, bool] = False,
) -> Iterator[VendorCredentials]:
    """Lists stored vendor credentials

     Lists stored vendor credentials, paginated and optionally filtered.

    Args:
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):
        vendor (Union[Unset, Vendor]):
        name (Union[Unset, str]):
        include_secrets (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Iterator[VendorCredentials]
    """

    response = sync(
        client=client,
        page_size=page_size,
        page_token=page_token,
        vendor=vendor,
        name=name,
        include_secrets=include_secrets,
    )
    while response is not None:
        yield from response.vendor_credentials

        page_token = response.next_page_token
        if page_token == UNSET:
            response = None
        else:
            response = sync(
                client=client,
                page_size=page_size,
                page_token=page_token,
                vendor=vendor,
                name=name,
                include_secrets=include_secrets,
            )


async def async_depaginated(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
    vendor: Union[Unset, Vendor] = UNSET,
    name: Union[Unset, str] = UNSET,
    include_secrets: Union[Unset, bool] = False,
) -> AsyncIterator[VendorCredentials]:
    """Lists stored vendor credentials

     Lists stored vendor credentials, paginated and optionally filtered.

    Args:
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):
        vendor (Union[Unset, Vendor]):
        name (Union[Unset, str]):
        include_secrets (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Iterator[VendorCredentials]
    """

    response = await asyncio(
        client=client,
        page_size=page_size,
        page_token=page_token,
        vendor=vendor,
        name=name,
        include_secrets=include_secrets,
    )
    while response is not None:
        for item in response.vendor_credentials:
            yield item

        page_token = response.next_page_token
        if page_token == UNSET:
            response = None
        else:
            response = await asyncio(
                client=client,
                page_size=page_size,
                page_token=page_token,
                vendor=vendor,
                name=name,
                include_secrets=include_secrets,
            )
