from typing import TYPE_CHECKING, Any, Dict, Literal, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.enphase_join_config_inline_credentials import EnphaseJoinConfigInlineCredentials
    from ..models.stored_credentials_reference import StoredCredentialsReference


T = TypeVar("T", bound="EnphaseJoinConfig")


@_attrs_define
class EnphaseJoinConfig:
    """
    Attributes:
        vendor (Literal['enphase']):
        credentials (Union['EnphaseJoinConfigInlineCredentials', 'StoredCredentialsReference']):
    """

    vendor: Literal["enphase"]
    credentials: Union["EnphaseJoinConfigInlineCredentials", "StoredCredentialsReference"]

    def to_dict(self) -> Dict[str, Any]:
        from ..models.enphase_join_config_inline_credentials import EnphaseJoinConfigInlineCredentials

        vendor = self.vendor

        credentials: Dict[str, Any]
        if isinstance(self.credentials, EnphaseJoinConfigInlineCredentials):
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
        from ..models.enphase_join_config_inline_credentials import EnphaseJoinConfigInlineCredentials
        from ..models.stored_credentials_reference import StoredCredentialsReference

        d = src_dict.copy()
        vendor = cast(Literal["enphase"], d.pop("vendor"))
        if vendor != "enphase":
            raise ValueError(f"vendor must match const 'enphase', got '{vendor}'")

        def _parse_credentials(
            data: object,
        ) -> Union["EnphaseJoinConfigInlineCredentials", "StoredCredentialsReference"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_enphase_join_config_credentials_type_0 = EnphaseJoinConfigInlineCredentials.from_dict(
                    data
                )

                return componentsschemas_enphase_join_config_credentials_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_enphase_join_config_credentials_type_1 = StoredCredentialsReference.from_dict(data)

            return componentsschemas_enphase_join_config_credentials_type_1

        credentials = _parse_credentials(d.pop("credentials"))

        enphase_join_config = cls(
            vendor=vendor,
            credentials=credentials,
        )

        return enphase_join_config
