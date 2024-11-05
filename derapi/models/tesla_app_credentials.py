from typing import Any, Dict, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="TeslaAppCredentials")


@_attrs_define
class TeslaAppCredentials:
    """
    Attributes:
        vendor (Literal['tesla']):  Default: 'tesla'.
        type (Literal['app']):  Default: 'app'.
        client_id (str): Client ID for a Tesla App
        client_secret (str): Client secret for a Tesla App
    """

    client_id: str
    client_secret: str
    vendor: Literal["tesla"] = "tesla"
    type: Literal["app"] = "app"

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
        vendor = cast(Literal["tesla"], d.pop("vendor"))
        if vendor != "tesla":
            raise ValueError(f"vendor must match const 'tesla', got '{vendor}'")

        type = cast(Literal["app"], d.pop("type"))
        if type != "app":
            raise ValueError(f"type must match const 'app', got '{type}'")

        client_id = d.pop("clientID")

        client_secret = d.pop("clientSecret")

        tesla_app_credentials = cls(
            vendor=vendor,
            type=type,
            client_id=client_id,
            client_secret=client_secret,
        )

        return tesla_app_credentials
