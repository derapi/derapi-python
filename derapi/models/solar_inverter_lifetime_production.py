import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

T = TypeVar("T", bound="SolarInverterLifetimeProduction")


@_attrs_define
class SolarInverterLifetimeProduction:
    """
    Attributes:
        kwh (float): Lifetime production value in kWh
        start (Union[None, datetime.datetime]): The start date of the lifetime production period in ISO-8601 format
    """

    kwh: float
    start: Union[None, datetime.datetime]

    def to_dict(self) -> Dict[str, Any]:
        kwh = self.kwh

        start: Union[None, str]
        if isinstance(self.start, datetime.datetime):
            start = self.start.isoformat()
        else:
            start = self.start

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

        def _parse_start(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_type_0 = isoparse(data)

                return start_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        start = _parse_start(d.pop("start"))

        solar_inverter_lifetime_production = cls(
            kwh=kwh,
            start=start,
        )

        return solar_inverter_lifetime_production
