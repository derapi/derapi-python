from typing import Any, Dict, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="HiddenSMASandboxCustomGrantCredentials")


@_attrs_define
class HiddenSMASandboxCustomGrantCredentials:
    """Credentials from the SMA Sandbox custom grant oauth flow

    Attributes:
        type (Literal['customgrant']):  Default: 'customgrant'.
        vendor (Literal['smasbox']):  Default: 'smasbox'.
    """

    type: Literal["customgrant"] = "customgrant"
    vendor: Literal["smasbox"] = "smasbox"

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

        vendor = cast(Literal["smasbox"], d.pop("vendor"))
        if vendor != "smasbox":
            raise ValueError(f"vendor must match const 'smasbox', got '{vendor}'")

        hidden_sma_sandbox_custom_grant_credentials = cls(
            type=type,
            vendor=vendor,
        )

        return hidden_sma_sandbox_custom_grant_credentials
