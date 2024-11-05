from typing import Any, Dict, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="HiddenSMAOAuthCredentials")


@_attrs_define
class HiddenSMAOAuthCredentials:
    """Credentials from the SMA OAuth code grant flow

    Attributes:
        type (Literal['oauthclient']):  Default: 'oauthclient'.
        vendor (Literal['sma']):  Default: 'sma'.
    """

    type: Literal["oauthclient"] = "oauthclient"
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
        type = cast(Literal["oauthclient"], d.pop("type"))
        if type != "oauthclient":
            raise ValueError(f"type must match const 'oauthclient', got '{type}'")

        vendor = cast(Literal["sma"], d.pop("vendor"))
        if vendor != "sma":
            raise ValueError(f"vendor must match const 'sma', got '{vendor}'")

        hidden_smao_auth_credentials = cls(
            type=type,
            vendor=vendor,
        )

        return hidden_smao_auth_credentials
