from typing import Any, Dict, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="FranklinWHCredentials")


@_attrs_define
class FranklinWHCredentials:
    """
    Attributes:
        vendor (Literal['franklinwh']):  Default: 'franklinwh'.
        type (Literal['partner']):  Default: 'partner'.
        client_id (str): FranklinWH Client ID
        client_secret (str): FranklinWH Client Secret
    """

    client_id: str
    client_secret: str
    vendor: Literal["franklinwh"] = "franklinwh"
    type: Literal["partner"] = "partner"

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
        vendor = cast(Literal["franklinwh"], d.pop("vendor"))
        if vendor != "franklinwh":
            raise ValueError(f"vendor must match const 'franklinwh', got '{vendor}'")

        type = cast(Literal["partner"], d.pop("type"))
        if type != "partner":
            raise ValueError(f"type must match const 'partner', got '{type}'")

        client_id = d.pop("clientID")

        client_secret = d.pop("clientSecret")

        franklin_wh_credentials = cls(
            vendor=vendor,
            type=type,
            client_id=client_id,
            client_secret=client_secret,
        )

        return franklin_wh_credentials
