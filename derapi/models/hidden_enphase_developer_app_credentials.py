from typing import Any, Dict, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="HiddenEnphaseDeveloperAppCredentials")


@_attrs_define
class HiddenEnphaseDeveloperAppCredentials:
    """
    Attributes:
        type (Literal['developerapp']):  Default: 'developerapp'.
        vendor (Literal['enphase']):  Default: 'enphase'.
    """

    type: Literal["developerapp"] = "developerapp"
    vendor: Literal["enphase"] = "enphase"

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
        type = cast(Literal["developerapp"], d.pop("type"))
        if type != "developerapp":
            raise ValueError(f"type must match const 'developerapp', got '{type}'")

        vendor = cast(Literal["enphase"], d.pop("vendor"))
        if vendor != "enphase":
            raise ValueError(f"vendor must match const 'enphase', got '{vendor}'")

        hidden_enphase_developer_app_credentials = cls(
            type=type,
            vendor=vendor,
        )

        return hidden_enphase_developer_app_credentials
