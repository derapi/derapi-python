from typing import TYPE_CHECKING, Any, Dict, Literal, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.sma_sandbox_join_config_inline_credentials import SMASandboxJoinConfigInlineCredentials
    from ..models.stored_credentials_reference import StoredCredentialsReference


T = TypeVar("T", bound="SMASandboxJoinConfig")


@_attrs_define
class SMASandboxJoinConfig:
    """
    Attributes:
        vendor (Literal['smasbox']):
        credentials (Union['SMASandboxJoinConfigInlineCredentials', 'StoredCredentialsReference']):
    """

    vendor: Literal["smasbox"]
    credentials: Union["SMASandboxJoinConfigInlineCredentials", "StoredCredentialsReference"]

    def to_dict(self) -> Dict[str, Any]:
        from ..models.sma_sandbox_join_config_inline_credentials import SMASandboxJoinConfigInlineCredentials

        vendor = self.vendor

        credentials: Dict[str, Any]
        if isinstance(self.credentials, SMASandboxJoinConfigInlineCredentials):
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
        from ..models.sma_sandbox_join_config_inline_credentials import SMASandboxJoinConfigInlineCredentials
        from ..models.stored_credentials_reference import StoredCredentialsReference

        d = src_dict.copy()
        vendor = cast(Literal["smasbox"], d.pop("vendor"))
        if vendor != "smasbox":
            raise ValueError(f"vendor must match const 'smasbox', got '{vendor}'")

        def _parse_credentials(
            data: object,
        ) -> Union["SMASandboxJoinConfigInlineCredentials", "StoredCredentialsReference"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credentials_type_0 = SMASandboxJoinConfigInlineCredentials.from_dict(data)

                return credentials_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            credentials_type_1 = StoredCredentialsReference.from_dict(data)

            return credentials_type_1

        credentials = _parse_credentials(d.pop("credentials"))

        sma_sandbox_join_config = cls(
            vendor=vendor,
            credentials=credentials,
        )

        return sma_sandbox_join_config
