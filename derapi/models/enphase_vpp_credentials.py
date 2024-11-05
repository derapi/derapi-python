from typing import Any, Dict, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="EnphaseVPPCredentials")


@_attrs_define
class EnphaseVPPCredentials:
    """
    Attributes:
        vendor (Literal['enphasevpp']):  Default: 'enphasevpp'.
        type (Literal['vpp']):  Default: 'vpp'.
        client_id (str): Enphase VPP Client ID
        client_secret (str): Enphase VPP Client Secret
        api_key (str): Enphase VPP API Key
    """

    client_id: str
    client_secret: str
    api_key: str
    vendor: Literal["enphasevpp"] = "enphasevpp"
    type: Literal["vpp"] = "vpp"

    def to_dict(self) -> Dict[str, Any]:
        vendor = self.vendor

        type = self.type

        client_id = self.client_id

        client_secret = self.client_secret

        api_key = self.api_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "vendor": vendor,
                "type": type,
                "clientID": client_id,
                "clientSecret": client_secret,
                "apiKey": api_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vendor = cast(Literal["enphasevpp"], d.pop("vendor"))
        if vendor != "enphasevpp":
            raise ValueError(f"vendor must match const 'enphasevpp', got '{vendor}'")

        type = cast(Literal["vpp"], d.pop("type"))
        if type != "vpp":
            raise ValueError(f"type must match const 'vpp', got '{type}'")

        client_id = d.pop("clientID")

        client_secret = d.pop("clientSecret")

        api_key = d.pop("apiKey")

        enphase_vpp_credentials = cls(
            vendor=vendor,
            type=type,
            client_id=client_id,
            client_secret=client_secret,
            api_key=api_key,
        )

        return enphase_vpp_credentials
