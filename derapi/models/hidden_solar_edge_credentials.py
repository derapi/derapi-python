from typing import Any, Dict, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="HiddenSolarEdgeCredentials")


@_attrs_define
class HiddenSolarEdgeCredentials:
    """
    Attributes:
        type (Literal['apikey']):  Default: 'apikey'.
        vendor (Literal['solaredge']):  Default: 'solaredge'.
    """

    type: Literal["apikey"] = "apikey"
    vendor: Literal["solaredge"] = "solaredge"

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        vendor = self.vendor

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "vendor": vendor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = cast(Literal["apikey"], d.pop("type"))
        if type != "apikey":
            raise ValueError(f"type must match const 'apikey', got '{type}'")

        vendor = cast(Literal["solaredge"], d.pop("vendor"))
        if vendor != "solaredge":
            raise ValueError(f"vendor must match const 'solaredge', got '{vendor}'")

        hidden_solar_edge_credentials = cls(
            type=type,
            vendor=vendor,
        )

        return hidden_solar_edge_credentials
