from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SolarInverterRecentErrorsInfo")


@_attrs_define
class SolarInverterRecentErrorsInfo:
    """
    Attributes:
        info (str):
    """

    info: str

    def to_dict(self) -> Dict[str, Any]:
        info = self.info

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "info": info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        info = d.pop("info")

        solar_inverter_recent_errors_info = cls(
            info=info,
        )

        return solar_inverter_recent_errors_info
