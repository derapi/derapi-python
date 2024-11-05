from typing import Any, Dict, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="HiddenEnphaseVPPCredentials")


@_attrs_define
class HiddenEnphaseVPPCredentials:
    """
    Attributes:
        type (Literal['vpp']):  Default: 'vpp'.
        vendor (Literal['enphasevpp']):  Default: 'enphasevpp'.
    """

    type: Literal["vpp"] = "vpp"
    vendor: Literal["enphasevpp"] = "enphasevpp"

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
        type = cast(Literal["vpp"], d.pop("type"))
        if type != "vpp":
            raise ValueError(f"type must match const 'vpp', got '{type}'")

        vendor = cast(Literal["enphasevpp"], d.pop("vendor"))
        if vendor != "enphasevpp":
            raise ValueError(f"vendor must match const 'enphasevpp', got '{vendor}'")

        hidden_enphase_vpp_credentials = cls(
            type=type,
            vendor=vendor,
        )

        return hidden_enphase_vpp_credentials
