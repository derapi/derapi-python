from typing import Any, Dict, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="SMASandboxOAuthCredentials")


@_attrs_define
class SMASandboxOAuthCredentials:
    """Credentials from the SMA Sandbox OAuth code grant flow

    Attributes:
        vendor (Literal['smasbox']):  Default: 'smasbox'.
        type (Literal['oauthclient']):  Default: 'oauthclient'.
        client_id (str): SMA Sandbox Client ID
        client_secret (str): SMA Sandbox Client Secret
    """

    client_id: str
    client_secret: str
    vendor: Literal["smasbox"] = "smasbox"
    type: Literal["oauthclient"] = "oauthclient"

    def to_dict(self) -> Dict[str, Any]:
        vendor = self.vendor

        type = self.type

        client_id = self.client_id

        client_secret = self.client_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "vendor": vendor,
                "type": type,
                "clientID": client_id,
                "clientSecret": client_secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vendor = cast(Literal["smasbox"], d.pop("vendor"))
        if vendor != "smasbox":
            raise ValueError(f"vendor must match const 'smasbox', got '{vendor}'")

        type = cast(Literal["oauthclient"], d.pop("type"))
        if type != "oauthclient":
            raise ValueError(f"type must match const 'oauthclient', got '{type}'")

        client_id = d.pop("clientID")

        client_secret = d.pop("clientSecret")

        sma_sandbox_o_auth_credentials = cls(
            vendor=vendor,
            type=type,
            client_id=client_id,
            client_secret=client_secret,
        )

        return sma_sandbox_o_auth_credentials
