from datetime import datetime, timedelta, timezone
from typing import Iterator

import pytest

from derapi.api.batteries import get_battery, get_battery_intervals, list_batteries
from derapi.api.virtual import create_virtual_battery, delete_virtual_battery
from derapi.client import Client
from derapi.models.create_virtual_battery_request import (
    CreateVirtualBatteryRequest,
)
from derapi.models.create_virtual_battery_response import (
    CreateVirtualBatteryResponse,
)
from derapi.models.vendor import Vendor
from derapi.models.virtual_battery import VirtualBattery


@pytest.fixture(scope="module")
def virtual_battery(virtual_client: Client) -> Iterator[CreateVirtualBatteryResponse]:
    virtual_battery = create_virtual_battery.sync(
        client=virtual_client,
        body=CreateVirtualBatteryRequest(name="My test battery"),
    )
    assert virtual_battery is not None

    yield virtual_battery

    delete_virtual_battery.sync_detailed(virtual_battery.id, client=virtual_client)


def test_get_battery(virtual_client: Client, virtual_battery: VirtualBattery) -> None:
    battery = get_battery.sync(virtual_battery.id, client=virtual_client)
    assert battery is not None

    assert battery.name == "My test battery"
    assert battery.vendor == Vendor.VIRTUAL


def test_list_batteries(virtual_client: Client, virtual_battery: VirtualBattery) -> None:
    batteries = list_batteries.sync_depaginated(client=virtual_client)
    assert any(battery.id == virtual_battery.id for battery in batteries)


def test_list_battery_intervals(
    virtual_client: Client,
    virtual_battery: VirtualBattery,
) -> None:
    intervals = get_battery_intervals.sync(
        virtual_battery.id,
        start=datetime.now(timezone.utc) - timedelta(hours=25),
        end=datetime.now(timezone.utc) - timedelta(hours=1),
        client=virtual_client,
    )
    assert intervals is not None

    assert len(intervals.intervals) > 0
    assert intervals.intervals[0].start.tzinfo is not None
