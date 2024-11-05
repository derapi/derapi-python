from typing import Any, Dict, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="HiddenSMASandboxOAuthCredentials")


@_attrs_define
class HiddenSMASandboxOAuthCredentials:
    """Credentials from the SMA Sandbox OAuth code grant flow

    Attributes:
        type (Literal['oauthclient']):  Default: 'oauthclient'.
        vendor (Literal['smasbox']):  Default: 'smasbox'.
    """

    type: Literal["oauthclient"] = "oauthclient"
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
        type = cast(Literal["oauthclient"], d.pop("type"))
        if type != "oauthclient":
            raise ValueError(f"type must match const 'oauthclient', got '{type}'")

        vendor = cast(Literal["smasbox"], d.pop("vendor"))
        if vendor != "smasbox":
            raise ValueError(f"vendor must match const 'smasbox', got '{vendor}'")

        hidden_sma_sandbox_o_auth_credentials = cls(
            type=type,
            vendor=vendor,
        )

        return hidden_sma_sandbox_o_auth_credentials
