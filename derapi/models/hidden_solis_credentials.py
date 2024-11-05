from typing import Any, Dict, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="HiddenSolisCredentials")


@_attrs_define
class HiddenSolisCredentials:
    """
    Attributes:
        type (Literal['apikeysecret']):  Default: 'apikeysecret'.
        vendor (Literal['solis']):  Default: 'solis'.
    """

    type: Literal["apikeysecret"] = "apikeysecret"
    vendor: Literal["solis"] = "solis"

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
        type = cast(Literal["apikeysecret"], d.pop("type"))
        if type != "apikeysecret":
            raise ValueError(f"type must match const 'apikeysecret', got '{type}'")

        vendor = cast(Literal["solis"], d.pop("vendor"))
        if vendor != "solis":
            raise ValueError(f"vendor must match const 'solis', got '{vendor}'")

        hidden_solis_credentials = cls(
            type=type,
            vendor=vendor,
        )

        return hidden_solis_credentials
