from typing import TYPE_CHECKING, Any, Dict, Literal, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.sma_join_config_inline_credentials import SMAJoinConfigInlineCredentials
    from ..models.stored_credentials_reference import StoredCredentialsReference


T = TypeVar("T", bound="SMAJoinConfig")


@_attrs_define
class SMAJoinConfig:
    """
    Attributes:
        vendor (Literal['sma']):
        credentials (Union['SMAJoinConfigInlineCredentials', 'StoredCredentialsReference']):
    """

    vendor: Literal["sma"]
    credentials: Union["SMAJoinConfigInlineCredentials", "StoredCredentialsReference"]

    def to_dict(self) -> Dict[str, Any]:
        from ..models.sma_join_config_inline_credentials import SMAJoinConfigInlineCredentials

        vendor = self.vendor

        credentials: Dict[str, Any]
        if isinstance(self.credentials, SMAJoinConfigInlineCredentials):
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
        from ..models.sma_join_config_inline_credentials import SMAJoinConfigInlineCredentials
        from ..models.stored_credentials_reference import StoredCredentialsReference

        d = src_dict.copy()
        vendor = cast(Literal["sma"], d.pop("vendor"))
        if vendor != "sma":
            raise ValueError(f"vendor must match const 'sma', got '{vendor}'")

        def _parse_credentials(data: object) -> Union["SMAJoinConfigInlineCredentials", "StoredCredentialsReference"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credentials_type_0 = SMAJoinConfigInlineCredentials.from_dict(data)

                return credentials_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            credentials_type_1 = StoredCredentialsReference.from_dict(data)

            return credentials_type_1

        credentials = _parse_credentials(d.pop("credentials"))

        sma_join_config = cls(
            vendor=vendor,
            credentials=credentials,
        )

        return sma_join_config
