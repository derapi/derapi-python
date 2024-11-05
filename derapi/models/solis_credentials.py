from typing import Any, Dict, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="SolisCredentials")


@_attrs_define
class SolisCredentials:
    """
    Attributes:
        vendor (Literal['solis']):  Default: 'solis'.
        type (Literal['apikeysecret']):  Default: 'apikeysecret'.
        key_id (str): Solis Key ID
        key_secret (str): Solis Secret
    """

    key_id: str
    key_secret: str
    vendor: Literal["solis"] = "solis"
    type: Literal["apikeysecret"] = "apikeysecret"

    def to_dict(self) -> Dict[str, Any]:
        vendor = self.vendor

        type = self.type

        key_id = self.key_id

        key_secret = self.key_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "vendor": vendor,
                "type": type,
                "keyID": key_id,
                "keySecret": key_secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vendor = cast(Literal["solis"], d.pop("vendor"))
        if vendor != "solis":
            raise ValueError(f"vendor must match const 'solis', got '{vendor}'")

        type = cast(Literal["apikeysecret"], d.pop("type"))
        if type != "apikeysecret":
            raise ValueError(f"type must match const 'apikeysecret', got '{type}'")

        key_id = d.pop("keyID")

        key_secret = d.pop("keySecret")

        solis_credentials = cls(
            vendor=vendor,
            type=type,
            key_id=key_id,
            key_secret=key_secret,
        )

        return solis_credentials
