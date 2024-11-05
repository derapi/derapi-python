from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="EnphaseVPPJoinConfigInlineCredentials")


@_attrs_define
class EnphaseVPPJoinConfigInlineCredentials:
    """
    Attributes:
        client_id (str): Enphase VPP Client ID
        client_secret (str): Enphase VPP Client Secret
        api_key (str): Enphase VPP API Key
    """

    client_id: str
    client_secret: str
    api_key: str

    def to_dict(self) -> Dict[str, Any]:
        client_id = self.client_id

        client_secret = self.client_secret

        api_key = self.api_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "clientID": client_id,
                "clientSecret": client_secret,
                "apiKey": api_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_id = d.pop("clientID")

        client_secret = d.pop("clientSecret")

        api_key = d.pop("apiKey")

        enphase_vpp_join_config_inline_credentials = cls(
            client_id=client_id,
            client_secret=client_secret,
            api_key=api_key,
        )

        return enphase_vpp_join_config_inline_credentials
