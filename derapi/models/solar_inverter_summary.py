from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SolarInverterSummary")


@_attrs_define
class SolarInverterSummary:
    """
    Attributes:
        id (str): ID of the solar inverter
    """

    id: str

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        solar_inverter_summary = cls(
            id=id,
        )

        return solar_inverter_summary
