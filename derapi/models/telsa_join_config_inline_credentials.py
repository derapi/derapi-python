from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="TelsaJoinConfigInlineCredentials")


@_attrs_define
class TelsaJoinConfigInlineCredentials:
    """
    Attributes:
        client_id (str): Client ID for a Tesla App
        client_secret (str): Client secret for a Tesla App
    """

    client_id: str
    client_secret: str

    def to_dict(self) -> Dict[str, Any]:
        client_id = self.client_id

        client_secret = self.client_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "clientID": client_id,
                "clientSecret": client_secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_id = d.pop("clientID")

        client_secret = d.pop("clientSecret")

        telsa_join_config_inline_credentials = cls(
            client_id=client_id,
            client_secret=client_secret,
        )

        return telsa_join_config_inline_credentials
