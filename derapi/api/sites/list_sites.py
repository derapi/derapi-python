from http import HTTPStatus
from typing import Any, AsyncIterator, Dict, Iterator, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_sites_response import ListSitesResponse
from ...models.site_summary import SiteSummary
from ...models.vendor import Vendor
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    vendor: Union[Unset, Vendor] = UNSET,
    vendor_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_vendor: Union[Unset, str] = UNSET
    if not isinstance(vendor, Unset):
        json_vendor = vendor.value

    params["vendor"] = json_vendor

    params["vendorID"] = vendor_id

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/sites",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListSitesResponse]:
    if response.status_code == 200:
        response_200 = ListSitesResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListSitesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    vendor: Union[Unset, Vendor] = UNSET,
    vendor_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
) -> Response[ListSitesResponse]:
    """Returns a list of Sites

     Returns a list of Sites. In the case a vendor API request encounters an error details are provided.

    Args:
        vendor (Union[Unset, Vendor]):
        vendor_id (Union[Unset, str]):
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListSitesResponse]
    """

    kwargs = _get_kwargs(
        vendor=vendor,
        vendor_id=vendor_id,
        page_size=page_size,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    vendor: Union[Unset, Vendor] = UNSET,
    vendor_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
) -> Optional[ListSitesResponse]:
    """Returns a list of Sites

     Returns a list of Sites. In the case a vendor API request encounters an error details are provided.

    Args:
        vendor (Union[Unset, Vendor]):
        vendor_id (Union[Unset, str]):
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListSitesResponse
    """

    return sync_detailed(
        client=client,
        vendor=vendor,
        vendor_id=vendor_id,
        page_size=page_size,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    vendor: Union[Unset, Vendor] = UNSET,
    vendor_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
) -> Response[ListSitesResponse]:
    """Returns a list of Sites

     Returns a list of Sites. In the case a vendor API request encounters an error details are provided.

    Args:
        vendor (Union[Unset, Vendor]):
        vendor_id (Union[Unset, str]):
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListSitesResponse]
    """

    kwargs = _get_kwargs(
        vendor=vendor,
        vendor_id=vendor_id,
        page_size=page_size,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    vendor: Union[Unset, Vendor] = UNSET,
    vendor_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
) -> Optional[ListSitesResponse]:
    """Returns a list of Sites

     Returns a list of Sites. In the case a vendor API request encounters an error details are provided.

    Args:
        vendor (Union[Unset, Vendor]):
        vendor_id (Union[Unset, str]):
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListSitesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            vendor=vendor,
            vendor_id=vendor_id,
            page_size=page_size,
            page_token=page_token,
        )
    ).parsed


def sync_depaginated(
    *,
    client: Union[AuthenticatedClient, Client],
    vendor: Union[Unset, Vendor] = UNSET,
    vendor_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
) -> Iterator[SiteSummary]:
    """Returns a list of Sites

     Returns a list of Sites. In the case a vendor API request encounters an error details are provided.

    Args:
        vendor (Union[Unset, Vendor]):
        vendor_id (Union[Unset, str]):
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Iterator[SiteSummary]
    """

    response = sync(
        client=client,
        vendor=vendor,
        vendor_id=vendor_id,
        page_size=page_size,
        page_token=page_token,
    )
    while response is not None:
        yield from response.sites

        page_token = response.next_page_token
        if page_token == UNSET:
            response = None
        else:
            response = sync(
                client=client,
                vendor=vendor,
                vendor_id=vendor_id,
                page_size=page_size,
                page_token=page_token,
            )


async def async_depaginated(
    *,
    client: Union[AuthenticatedClient, Client],
    vendor: Union[Unset, Vendor] = UNSET,
    vendor_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
) -> AsyncIterator[SiteSummary]:
    """Returns a list of Sites

     Returns a list of Sites. In the case a vendor API request encounters an error details are provided.

    Args:
        vendor (Union[Unset, Vendor]):
        vendor_id (Union[Unset, str]):
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Iterator[SiteSummary]
    """

    response = await asyncio(
        client=client,
        vendor=vendor,
        vendor_id=vendor_id,
        page_size=page_size,
        page_token=page_token,
    )
    while response is not None:
        for item in response.sites:
            yield item

        page_token = response.next_page_token
        if page_token == UNSET:
            response = None
        else:
            response = await asyncio(
                client=client,
                vendor=vendor,
                vendor_id=vendor_id,
                page_size=page_size,
                page_token=page_token,
            )
