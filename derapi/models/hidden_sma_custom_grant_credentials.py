from typing import Any, Dict, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="HiddenSMACustomGrantCredentials")


@_attrs_define
class HiddenSMACustomGrantCredentials:
    """Credentials from the SMA custom grant oauth flow

    Attributes:
        type (Literal['customgrant']):  Default: 'customgrant'.
        vendor (Literal['sma']):  Default: 'sma'.
    """

    type: Literal["customgrant"] = "customgrant"
    vendor: Literal["sma"] = "sma"

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
        type = cast(Literal["customgrant"], d.pop("type"))
        if type != "customgrant":
            raise ValueError(f"type must match const 'customgrant', got '{type}'")

        vendor = cast(Literal["sma"], d.pop("vendor"))
        if vendor != "sma":
            raise ValueError(f"vendor must match const 'sma', got '{vendor}'")

        hidden_sma_custom_grant_credentials = cls(
            type=type,
            vendor=vendor,
        )

        return hidden_sma_custom_grant_credentials
