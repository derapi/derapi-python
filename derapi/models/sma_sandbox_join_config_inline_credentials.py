from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SMASandboxJoinConfigInlineCredentials")


@_attrs_define
class SMASandboxJoinConfigInlineCredentials:
    """
    Attributes:
        client_id (str): SMA Sandbox Client ID
        client_secret (str): SMA Sandbox Client Secret
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

        sma_sandbox_join_config_inline_credentials = cls(
            client_id=client_id,
            client_secret=client_secret,
        )

        return sma_sandbox_join_config_inline_credentials
