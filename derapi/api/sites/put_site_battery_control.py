from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_site_battery_control_request import PutSiteBatteryControlRequest
from ...models.put_site_battery_control_response import PutSiteBatteryControlResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: PutSiteBatteryControlRequest,
    program_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["programID"] = program_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/sites/{id}/battery-control",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PutSiteBatteryControlResponse]:
    if response.status_code == 200:
        response_200 = PutSiteBatteryControlResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PutSiteBatteryControlResponse]:
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
    body: PutSiteBatteryControlRequest,
    program_id: Union[Unset, str] = UNSET,
) -> Response[PutSiteBatteryControlResponse]:
    """Accepts Battery control signals for an individual Site

     Accepts Battery control signals for individual Sites and translates those to vendor control
    commands.

    Args:
        id (str): the ID for the Site
        program_id (Union[Unset, str]):
        body (PutSiteBatteryControlRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutSiteBatteryControlResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        program_id=program_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PutSiteBatteryControlRequest,
    program_id: Union[Unset, str] = UNSET,
) -> Optional[PutSiteBatteryControlResponse]:
    """Accepts Battery control signals for an individual Site

     Accepts Battery control signals for individual Sites and translates those to vendor control
    commands.

    Args:
        id (str): the ID for the Site
        program_id (Union[Unset, str]):
        body (PutSiteBatteryControlRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutSiteBatteryControlResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        program_id=program_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PutSiteBatteryControlRequest,
    program_id: Union[Unset, str] = UNSET,
) -> Response[PutSiteBatteryControlResponse]:
    """Accepts Battery control signals for an individual Site

     Accepts Battery control signals for individual Sites and translates those to vendor control
    commands.

    Args:
        id (str): the ID for the Site
        program_id (Union[Unset, str]):
        body (PutSiteBatteryControlRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutSiteBatteryControlResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        program_id=program_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PutSiteBatteryControlRequest,
    program_id: Union[Unset, str] = UNSET,
) -> Optional[PutSiteBatteryControlResponse]:
    """Accepts Battery control signals for an individual Site

     Accepts Battery control signals for individual Sites and translates those to vendor control
    commands.

    Args:
        id (str): the ID for the Site
        program_id (Union[Unset, str]):
        body (PutSiteBatteryControlRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutSiteBatteryControlResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            program_id=program_id,
        )
    ).parsed
