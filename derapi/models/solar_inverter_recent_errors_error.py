from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SolarInverterRecentErrorsError")


@_attrs_define
class SolarInverterRecentErrorsError:
    """
    Attributes:
        error (str):
    """

    error: str

    def to_dict(self) -> Dict[str, Any]:
        error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error = d.pop("error")

        solar_inverter_recent_errors_error = cls(
            error=error,
        )

        return solar_inverter_recent_errors_error
