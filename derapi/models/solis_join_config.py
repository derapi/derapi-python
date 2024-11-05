from typing import Any, Dict, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="SolisJoinConfig")


@_attrs_define
class SolisJoinConfig:
    """
    Attributes:
        vendor (Literal['solis']):
    """

    vendor: Literal["solis"]

    def to_dict(self) -> Dict[str, Any]:
        vendor = self.vendor

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "vendor": vendor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vendor = cast(Literal["solis"], d.pop("vendor"))
        if vendor != "solis":
            raise ValueError(f"vendor must match const 'solis', got '{vendor}'")

        solis_join_config = cls(
            vendor=vendor,
        )

        return solis_join_config
