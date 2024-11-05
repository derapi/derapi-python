from typing import Any, Dict, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="HiddenFranklinWHCredentials")


@_attrs_define
class HiddenFranklinWHCredentials:
    """
    Attributes:
        type (Literal['partner']):  Default: 'partner'.
        vendor (Literal['franklinwh']):  Default: 'franklinwh'.
    """

    type: Literal["partner"] = "partner"
    vendor: Literal["franklinwh"] = "franklinwh"

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        vendor = self.vendor

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "vendor": vendor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = cast(Literal["partner"], d.pop("type"))
        if type != "partner":
            raise ValueError(f"type must match const 'partner', got '{type}'")

        vendor = cast(Literal["franklinwh"], d.pop("vendor"))
        if vendor != "franklinwh":
            raise ValueError(f"vendor must match const 'franklinwh', got '{vendor}'")

        hidden_franklin_wh_credentials = cls(
            type=type,
            vendor=vendor,
        )

        return hidden_franklin_wh_credentials
