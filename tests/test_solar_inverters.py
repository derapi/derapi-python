from datetime import datetime, timedelta, timezone
from typing import Iterator

import pytest

from derapi.api.solar_inverters import (
    get_solar_inverter,
    get_solar_inverter_intervals,
    list_solar_inverters,
)
from derapi.api.virtual import (
    create_virtual_solar_inverter,
    delete_virtual_solar_inverter,
)
from derapi.client import Client
from derapi.models.create_virtual_solar_inverter_request import (
    CreateVirtualSolarInverterRequest,
)
from derapi.models.create_virtual_solar_inverter_response import (
    CreateVirtualSolarInverterResponse,
)
from derapi.models.vendor import Vendor
from derapi.models.virtual_solar_inverter import VirtualSolarInverter


@pytest.fixture(scope="module")
def virtual_inverter(virtual_client: Client) -> Iterator[CreateVirtualSolarInverterResponse]:
    virtual_inverter = create_virtual_solar_inverter.sync(
        client=virtual_client,
        body=CreateVirtualSolarInverterRequest(name="My test inverter"),
    )
    assert virtual_inverter is not None

    yield virtual_inverter

    delete_virtual_solar_inverter.sync_detailed(virtual_inverter.id, client=virtual_client)


def test_get_solar_inverter(
    virtual_client: Client,
    virtual_inverter: VirtualSolarInverter,
) -> None:
    inverter = get_solar_inverter.sync(virtual_inverter.id, client=virtual_client)
    assert inverter is not None

    assert inverter.name == "My test inverter"
    assert inverter.vendor == Vendor.VIRTUAL


def test_list_solar_inverters(
    virtual_client: Client,
    virtual_inverter: CreateVirtualSolarInverterResponse,
) -> None:
    inverters = list_solar_inverters.sync_depaginated(client=virtual_client)
    assert inverters is not None

    assert any(inverter.id == virtual_inverter.id for inverter in inverters)


def test_list_solar_inverter_intervals(
    virtual_client: Client,
    virtual_inverter: CreateVirtualSolarInverterResponse,
) -> None:
    intervals = get_solar_inverter_intervals.sync(
        virtual_inverter.id,
        start=datetime.now(timezone.utc) - timedelta(hours=25),
        end=datetime.now(timezone.utc) - timedelta(hours=1),
        client=virtual_client,
    )
    assert intervals is not None

    assert len(intervals.intervals) > 0
    assert intervals.intervals[0].start.tzinfo is not None
