from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="StoredCredentialsReference")


@_attrs_define
class StoredCredentialsReference:
    """
    Attributes:
        credentials_id (str): ID for the vendor credentials
    """

    credentials_id: str

    def to_dict(self) -> Dict[str, Any]:
        credentials_id = self.credentials_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "credentialsID": credentials_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        credentials_id = d.pop("credentialsID")

        stored_credentials_reference = cls(
            credentials_id=credentials_id,
        )

        return stored_credentials_reference
