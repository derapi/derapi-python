import datetime
from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

T = TypeVar("T", bound="SiteSolarInverterInterval")


@_attrs_define
class SiteSolarInverterInterval:
    """
    Attributes:
        kwh (float): Solar energy production in kWh
        start (datetime.datetime): Interval start in ISO-8601 format
        end (datetime.datetime): Interval end in ISO-8601 format
    """

    kwh: float
    start: datetime.datetime
    end: datetime.datetime

    def to_dict(self) -> Dict[str, Any]:
        kwh = self.kwh

        start = self.start.isoformat()

        end = self.end.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "kwh": kwh,
                "start": start,
                "end": end,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        kwh = d.pop("kwh")

        start = isoparse(d.pop("start"))

        end = isoparse(d.pop("end"))

        site_solar_inverter_interval = cls(
            kwh=kwh,
            start=start,
            end=end,
        )

        return site_solar_inverter_interval
