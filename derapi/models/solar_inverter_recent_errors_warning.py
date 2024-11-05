from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SolarInverterRecentErrorsWarning")


@_attrs_define
class SolarInverterRecentErrorsWarning:
    """
    Attributes:
        warning (str):
    """

    warning: str

    def to_dict(self) -> Dict[str, Any]:
        warning = self.warning

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "warning": warning,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        warning = d.pop("warning")

        solar_inverter_recent_errors_warning = cls(
            warning=warning,
        )

        return solar_inverter_recent_errors_warning
