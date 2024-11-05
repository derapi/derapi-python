import datetime
from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

T = TypeVar("T", bound="SolarInverterRecentProduction")


@_attrs_define
class SolarInverterRecentProduction:
    """
    Attributes:
        kwh (float): Recent production value in kWh
        start (datetime.datetime): The start date of the recent production period in ISO-8601 format
    """

    kwh: float
    start: datetime.datetime

    def to_dict(self) -> Dict[str, Any]:
        kwh = self.kwh

        start = self.start.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "kwh": kwh,
                "start": start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        kwh = d.pop("kwh")

        start = isoparse(d.pop("start"))

        solar_inverter_recent_production = cls(
            kwh=kwh,
            start=start,
        )

        return solar_inverter_recent_production
