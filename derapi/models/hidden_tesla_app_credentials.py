from typing import Any, Dict, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="HiddenTeslaAppCredentials")


@_attrs_define
class HiddenTeslaAppCredentials:
    """
    Attributes:
        type (Literal['app']):  Default: 'app'.
        vendor (Literal['tesla']):  Default: 'tesla'.
    """

    type: Literal["app"] = "app"
    vendor: Literal["tesla"] = "tesla"

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
        type = cast(Literal["app"], d.pop("type"))
        if type != "app":
            raise ValueError(f"type must match const 'app', got '{type}'")

        vendor = cast(Literal["tesla"], d.pop("vendor"))
        if vendor != "tesla":
            raise ValueError(f"vendor must match const 'tesla', got '{vendor}'")

        hidden_tesla_app_credentials = cls(
            type=type,
            vendor=vendor,
        )

        return hidden_tesla_app_credentials
