from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_virtual_battery_request import CreateVirtualBatteryRequest
from ...models.create_virtual_battery_response import CreateVirtualBatteryResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateVirtualBatteryRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/virtual/batteries",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CreateVirtualBatteryResponse]:
    if response.status_code == 201:
        response_201 = CreateVirtualBatteryResponse.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CreateVirtualBatteryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateVirtualBatteryRequest,
) -> Response[CreateVirtualBatteryResponse]:
    """Create a Virtual Battery

     Create Virtual Battery test configuration in the current sandbox.

    Args:
        body (CreateVirtualBatteryRequest): Fields the user would like to provide. Omitted ones
            will be inferred.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateVirtualBatteryResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateVirtualBatteryRequest,
) -> Optional[CreateVirtualBatteryResponse]:
    """Create a Virtual Battery

     Create Virtual Battery test configuration in the current sandbox.

    Args:
        body (CreateVirtualBatteryRequest): Fields the user would like to provide. Omitted ones
            will be inferred.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateVirtualBatteryResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateVirtualBatteryRequest,
) -> Response[CreateVirtualBatteryResponse]:
    """Create a Virtual Battery

     Create Virtual Battery test configuration in the current sandbox.

    Args:
        body (CreateVirtualBatteryRequest): Fields the user would like to provide. Omitted ones
            will be inferred.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateVirtualBatteryResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateVirtualBatteryRequest,
) -> Optional[CreateVirtualBatteryResponse]:
    """Create a Virtual Battery

     Create Virtual Battery test configuration in the current sandbox.

    Args:
        body (CreateVirtualBatteryRequest): Fields the user would like to provide. Omitted ones
            will be inferred.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateVirtualBatteryResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
