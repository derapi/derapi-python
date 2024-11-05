from typing import TYPE_CHECKING, Any, Dict, Literal, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.stored_credentials_reference import StoredCredentialsReference
    from ..models.telsa_join_config_inline_credentials import TelsaJoinConfigInlineCredentials


T = TypeVar("T", bound="TeslaJoinConfig")


@_attrs_define
class TeslaJoinConfig:
    """
    Attributes:
        vendor (Literal['tesla']):
        credentials (Union['StoredCredentialsReference', 'TelsaJoinConfigInlineCredentials']):
    """

    vendor: Literal["tesla"]
    credentials: Union["StoredCredentialsReference", "TelsaJoinConfigInlineCredentials"]

    def to_dict(self) -> Dict[str, Any]:
        from ..models.telsa_join_config_inline_credentials import TelsaJoinConfigInlineCredentials

        vendor = self.vendor

        credentials: Dict[str, Any]
        if isinstance(self.credentials, TelsaJoinConfigInlineCredentials):
            credentials = self.credentials.to_dict()
        else:
            credentials = self.credentials.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "vendor": vendor,
                "credentials": credentials,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stored_credentials_reference import StoredCredentialsReference
        from ..models.telsa_join_config_inline_credentials import TelsaJoinConfigInlineCredentials

        d = src_dict.copy()
        vendor = cast(Literal["tesla"], d.pop("vendor"))
        if vendor != "tesla":
            raise ValueError(f"vendor must match const 'tesla', got '{vendor}'")

        def _parse_credentials(data: object) -> Union["StoredCredentialsReference", "TelsaJoinConfigInlineCredentials"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credentials_type_0 = TelsaJoinConfigInlineCredentials.from_dict(data)

                return credentials_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            credentials_type_1 = StoredCredentialsReference.from_dict(data)

            return credentials_type_1

        credentials = _parse_credentials(d.pop("credentials"))

        tesla_join_config = cls(
            vendor=vendor,
            credentials=credentials,
        )

        return tesla_join_config
