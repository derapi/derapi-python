from typing import Any, Dict, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="HiddenEnphasePartnerAppCredentials")


@_attrs_define
class HiddenEnphasePartnerAppCredentials:
    """Credentials for an Enphase partner app

    Attributes:
        type (Literal['partnerapp']):  Default: 'partnerapp'.
        vendor (Literal['enphase']):  Default: 'enphase'.
    """

    type: Literal["partnerapp"] = "partnerapp"
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
        type = cast(Literal["partnerapp"], d.pop("type"))
        if type != "partnerapp":
            raise ValueError(f"type must match const 'partnerapp', got '{type}'")

        vendor = cast(Literal["enphase"], d.pop("vendor"))
        if vendor != "enphase":
            raise ValueError(f"vendor must match const 'enphase', got '{vendor}'")

        hidden_enphase_partner_app_credentials = cls(
            type=type,
            vendor=vendor,
        )

        return hidden_enphase_partner_app_credentials
