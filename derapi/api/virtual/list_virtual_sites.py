from http import HTTPStatus
from typing import Any, AsyncIterator, Dict, Iterator, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_virtual_sites_response import ListVirtualSitesResponse
from ...models.virtual_site import VirtualSite
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/virtual/sites",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListVirtualSitesResponse]:
    if response.status_code == 200:
        response_200 = ListVirtualSitesResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListVirtualSitesResponse]:
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
) -> Response[ListVirtualSitesResponse]:
    """List Virtual Sites

     List Virtual Site test configurations in the current sandbox.

    Args:
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListVirtualSitesResponse]
    """

    kwargs = _get_kwargs(
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
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
) -> Optional[ListVirtualSitesResponse]:
    """List Virtual Sites

     List Virtual Site test configurations in the current sandbox.

    Args:
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListVirtualSitesResponse
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
) -> Response[ListVirtualSitesResponse]:
    """List Virtual Sites

     List Virtual Site test configurations in the current sandbox.

    Args:
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListVirtualSitesResponse]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
) -> Optional[ListVirtualSitesResponse]:
    """List Virtual Sites

     List Virtual Site test configurations in the current sandbox.

    Args:
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListVirtualSitesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            page_token=page_token,
        )
    ).parsed


def sync_depaginated(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
) -> Iterator[VirtualSite]:
    """List Virtual Sites

     List Virtual Site test configurations in the current sandbox.

    Args:
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Iterator[VirtualSite]
    """

    response = sync(
        client=client,
        page_size=page_size,
        page_token=page_token,
    )
    while response is not None:
        yield from response.virtual_sites

        page_token = response.next_page_token
        if page_token == UNSET:
            response = None
        else:
            response = sync(
                client=client,
                page_size=page_size,
                page_token=page_token,
            )


async def async_depaginated(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
) -> AsyncIterator[VirtualSite]:
    """List Virtual Sites

     List Virtual Site test configurations in the current sandbox.

    Args:
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Iterator[VirtualSite]
    """

    response = await asyncio(
        client=client,
        page_size=page_size,
        page_token=page_token,
    )
    while response is not None:
        for item in response.virtual_sites:
            yield item

        page_token = response.next_page_token
        if page_token == UNSET:
            response = None
        else:
            response = await asyncio(
                client=client,
                page_size=page_size,
                page_token=page_token,
            )
