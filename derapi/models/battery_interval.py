import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatteryInterval")


@_attrs_define
class BatteryInterval:
    """
    Attributes:
        charge_kwh (float): kWh into the Battery during the interval
        discharge_kwh (float): kWh out of the Battery during the interval
        start (datetime.datetime): Interval start in ISO-8601 format
        end (datetime.datetime): Interval end in ISO-8601 format
        state_of_charge_percent (Union[Unset, float]): average % charge over the interval
    """

    charge_kwh: float
    discharge_kwh: float
    start: datetime.datetime
    end: datetime.datetime
    state_of_charge_percent: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        charge_kwh = self.charge_kwh

        discharge_kwh = self.discharge_kwh

        start = self.start.isoformat()

        end = self.end.isoformat()

        state_of_charge_percent = self.state_of_charge_percent

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "chargeKwh": charge_kwh,
                "dischargeKwh": discharge_kwh,
                "start": start,
                "end": end,
            }
        )
        if state_of_charge_percent is not UNSET:
            field_dict["stateOfChargePercent"] = state_of_charge_percent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        charge_kwh = d.pop("chargeKwh")

        discharge_kwh = d.pop("dischargeKwh")

        start = isoparse(d.pop("start"))

        end = isoparse(d.pop("end"))

        state_of_charge_percent = d.pop("stateOfChargePercent", UNSET)

        battery_interval = cls(
            charge_kwh=charge_kwh,
            discharge_kwh=discharge_kwh,
            start=start,
            end=end,
            state_of_charge_percent=state_of_charge_percent,
        )

        return battery_interval
