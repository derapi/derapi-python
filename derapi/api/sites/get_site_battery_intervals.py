import datetime
from http import HTTPStatus
from typing import Any, AsyncIterator, Dict, Iterator, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_site_battery_intervals_response import GetSiteBatteryIntervalsResponse
from ...models.site_battery_interval import SiteBatteryInterval
from ...models.summary_level import SummaryLevel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    summary_level: Union[Unset, SummaryLevel] = UNSET,
    start: datetime.datetime,
    end: datetime.datetime,
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_summary_level: Union[Unset, str] = UNSET
    if not isinstance(summary_level, Unset):
        json_summary_level = summary_level.value

    params["summaryLevel"] = json_summary_level

    json_start = start.isoformat()
    params["start"] = json_start

    json_end = end.isoformat()
    params["end"] = json_end

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/sites/{id}/battery-intervals",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetSiteBatteryIntervalsResponse]:
    if response.status_code == 200:
        response_200 = GetSiteBatteryIntervalsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetSiteBatteryIntervalsResponse]:
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
    summary_level: Union[Unset, SummaryLevel] = UNSET,
    start: datetime.datetime,
    end: datetime.datetime,
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
) -> Response[GetSiteBatteryIntervalsResponse]:
    """Returns Battery system interval data

     Returns Site-level Battery charge and discharge data aggregated to the specific granularity
    requested for a specified start and end date. The energy data intervals are represented in kWh.
    Intervals are always aligned with the start of a month, day, or hour. Partial period requests are
    expanded to cover the full interval for the requested summary level. For example, a summary-level
    request of month with a start date of 12/3 and end date of 1/1 will return data covering the entire
    month of December.

    Args:
        id (str): the ID for the Site
        summary_level (Union[Unset, SummaryLevel]):
        start (datetime.datetime):
        end (datetime.datetime):
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSiteBatteryIntervalsResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        summary_level=summary_level,
        start=start,
        end=end,
        page_size=page_size,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    summary_level: Union[Unset, SummaryLevel] = UNSET,
    start: datetime.datetime,
    end: datetime.datetime,
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
) -> Optional[GetSiteBatteryIntervalsResponse]:
    """Returns Battery system interval data

     Returns Site-level Battery charge and discharge data aggregated to the specific granularity
    requested for a specified start and end date. The energy data intervals are represented in kWh.
    Intervals are always aligned with the start of a month, day, or hour. Partial period requests are
    expanded to cover the full interval for the requested summary level. For example, a summary-level
    request of month with a start date of 12/3 and end date of 1/1 will return data covering the entire
    month of December.

    Args:
        id (str): the ID for the Site
        summary_level (Union[Unset, SummaryLevel]):
        start (datetime.datetime):
        end (datetime.datetime):
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSiteBatteryIntervalsResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        summary_level=summary_level,
        start=start,
        end=end,
        page_size=page_size,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    summary_level: Union[Unset, SummaryLevel] = UNSET,
    start: datetime.datetime,
    end: datetime.datetime,
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
) -> Response[GetSiteBatteryIntervalsResponse]:
    """Returns Battery system interval data

     Returns Site-level Battery charge and discharge data aggregated to the specific granularity
    requested for a specified start and end date. The energy data intervals are represented in kWh.
    Intervals are always aligned with the start of a month, day, or hour. Partial period requests are
    expanded to cover the full interval for the requested summary level. For example, a summary-level
    request of month with a start date of 12/3 and end date of 1/1 will return data covering the entire
    month of December.

    Args:
        id (str): the ID for the Site
        summary_level (Union[Unset, SummaryLevel]):
        start (datetime.datetime):
        end (datetime.datetime):
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSiteBatteryIntervalsResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        summary_level=summary_level,
        start=start,
        end=end,
        page_size=page_size,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    summary_level: Union[Unset, SummaryLevel] = UNSET,
    start: datetime.datetime,
    end: datetime.datetime,
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
) -> Optional[GetSiteBatteryIntervalsResponse]:
    """Returns Battery system interval data

     Returns Site-level Battery charge and discharge data aggregated to the specific granularity
    requested for a specified start and end date. The energy data intervals are represented in kWh.
    Intervals are always aligned with the start of a month, day, or hour. Partial period requests are
    expanded to cover the full interval for the requested summary level. For example, a summary-level
    request of month with a start date of 12/3 and end date of 1/1 will return data covering the entire
    month of December.

    Args:
        id (str): the ID for the Site
        summary_level (Union[Unset, SummaryLevel]):
        start (datetime.datetime):
        end (datetime.datetime):
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSiteBatteryIntervalsResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            summary_level=summary_level,
            start=start,
            end=end,
            page_size=page_size,
            page_token=page_token,
        )
    ).parsed


def sync_depaginated(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    summary_level: Union[Unset, SummaryLevel] = UNSET,
    start: datetime.datetime,
    end: datetime.datetime,
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
) -> Iterator[SiteBatteryInterval]:
    """Returns Battery system interval data

     Returns Site-level Battery charge and discharge data aggregated to the specific granularity
    requested for a specified start and end date. The energy data intervals are represented in kWh.
    Intervals are always aligned with the start of a month, day, or hour. Partial period requests are
    expanded to cover the full interval for the requested summary level. For example, a summary-level
    request of month with a start date of 12/3 and end date of 1/1 will return data covering the entire
    month of December.

    Args:
        id (str): the ID for the Site
        summary_level (Union[Unset, SummaryLevel]):
        start (datetime.datetime):
        end (datetime.datetime):
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Iterator[SiteBatteryInterval]
    """

    response = sync(
        id=id,
        client=client,
        summary_level=summary_level,
        start=start,
        end=end,
        page_size=page_size,
        page_token=page_token,
    )
    while response is not None:
        yield from response.intervals

        page_token = response.next_page_token
        if page_token == UNSET:
            response = None
        else:
            response = sync(
                id=id,
                client=client,
                summary_level=summary_level,
                start=start,
                end=end,
                page_size=page_size,
                page_token=page_token,
            )


async def async_depaginated(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    summary_level: Union[Unset, SummaryLevel] = UNSET,
    start: datetime.datetime,
    end: datetime.datetime,
    page_size: Union[Unset, int] = 50,
    page_token: Union[Unset, str] = UNSET,
) -> AsyncIterator[SiteBatteryInterval]:
    """Returns Battery system interval data

     Returns Site-level Battery charge and discharge data aggregated to the specific granularity
    requested for a specified start and end date. The energy data intervals are represented in kWh.
    Intervals are always aligned with the start of a month, day, or hour. Partial period requests are
    expanded to cover the full interval for the requested summary level. For example, a summary-level
    request of month with a start date of 12/3 and end date of 1/1 will return data covering the entire
    month of December.

    Args:
        id (str): the ID for the Site
        summary_level (Union[Unset, SummaryLevel]):
        start (datetime.datetime):
        end (datetime.datetime):
        page_size (Union[Unset, int]):  Default: 50.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Iterator[SiteBatteryInterval]
    """

    response = await asyncio(
        id=id,
        client=client,
        summary_level=summary_level,
        start=start,
        end=end,
        page_size=page_size,
        page_token=page_token,
    )
    while response is not None:
        for item in response.intervals:
            yield item

        page_token = response.next_page_token
        if page_token == UNSET:
            response = None
        else:
            response = await asyncio(
                id=id,
                client=client,
                summary_level=summary_level,
                start=start,
                end=end,
                page_size=page_size,
                page_token=page_token,
            )
