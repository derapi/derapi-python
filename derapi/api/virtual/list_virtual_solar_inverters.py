from http import HTTPStatus
from typing import Any, AsyncIterator, Dict, Iterator, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_virtual_solar_inverters_response import ListVirtualSolarInvertersResponse
from ...models.virtual_solar_inverter import VirtualSolarInverter
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
        "url": "/virtual/solar-inverters",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListVirtualSolarInvertersResponse]:
    if response.status_code == 200:
        response_200 = ListVirtualSolarInvertersResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListVirtualSolarInvertersResponse]:
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
) -> Response[ListVirtualSolarInvertersResponse]:
    """List virtual solar inverters

     List virtual solar inverter test configurations in the current sandbox.

    Args:
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListVirtualSolarInvertersResponse]
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
) -> Optional[ListVirtualSolarInvertersResponse]:
    """List virtual solar inverters

     List virtual solar inverter test configurations in the current sandbox.

    Args:
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListVirtualSolarInvertersResponse
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
) -> Response[ListVirtualSolarInvertersResponse]:
    """List virtual solar inverters

     List virtual solar inverter test configurations in the current sandbox.

    Args:
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListVirtualSolarInvertersResponse]
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
) -> Optional[ListVirtualSolarInvertersResponse]:
    """List virtual solar inverters

     List virtual solar inverter test configurations in the current sandbox.

    Args:
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListVirtualSolarInvertersResponse
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
) -> Iterator[VirtualSolarInverter]:
    """List virtual solar inverters

     List virtual solar inverter test configurations in the current sandbox.

    Args:
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Iterator[VirtualSolarInverter]
    """

    response = sync(
        client=client,
        page_size=page_size,
        page_token=page_token,
    )
    while response is not None:
        yield from response.virtual_solar_inverters

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
) -> AsyncIterator[VirtualSolarInverter]:
    """List virtual solar inverters

     List virtual solar inverter test configurations in the current sandbox.

    Args:
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Iterator[VirtualSolarInverter]
    """

    response = await asyncio(
        client=client,
        page_size=page_size,
        page_token=page_token,
    )
    while response is not None:
        for item in response.virtual_solar_inverters:
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
