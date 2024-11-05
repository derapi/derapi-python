from typing import Any, Dict, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="EnphasePartnerAppCredentials")


@_attrs_define
class EnphasePartnerAppCredentials:
    """Credentials for an Enphase partner app

    Attributes:
        vendor (Literal['enphase']):  Default: 'enphase'.
        type (Literal['partnerapp']):  Default: 'partnerapp'.
        client_id (str): Enphase Client ID
        client_secret (str): Enphase Client Secret
        api_key (str): Enphase API key of the application
    """

    client_id: str
    client_secret: str
    api_key: str
    vendor: Literal["enphase"] = "enphase"
    type: Literal["partnerapp"] = "partnerapp"

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
        vendor = cast(Literal["enphase"], d.pop("vendor"))
        if vendor != "enphase":
            raise ValueError(f"vendor must match const 'enphase', got '{vendor}'")

        type = cast(Literal["partnerapp"], d.pop("type"))
        if type != "partnerapp":
            raise ValueError(f"type must match const 'partnerapp', got '{type}'")

        client_id = d.pop("clientID")

        client_secret = d.pop("clientSecret")

        api_key = d.pop("apiKey")

        enphase_partner_app_credentials = cls(
            vendor=vendor,
            type=type,
            client_id=client_id,
            client_secret=client_secret,
            api_key=api_key,
        )

        return enphase_partner_app_credentials
