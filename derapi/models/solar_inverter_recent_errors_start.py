import datetime
from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

T = TypeVar("T", bound="SolarInverterRecentErrorsStart")


@_attrs_define
class SolarInverterRecentErrorsStart:
    """
    Attributes:
        start (datetime.datetime): The start date of the recent errors log in ISO-8601 format
    """

    start: datetime.datetime

    def to_dict(self) -> Dict[str, Any]:
        start = self.start.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "start": start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start = isoparse(d.pop("start"))

        solar_inverter_recent_errors_start = cls(
            start=start,
        )

        return solar_inverter_recent_errors_start
