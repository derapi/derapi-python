from typing import Any, Dict, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="SolaredgeJoinConfig")


@_attrs_define
class SolaredgeJoinConfig:
    """
    Attributes:
        vendor (Literal['solaredge']):
    """

    vendor: Literal["solaredge"]

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
        vendor = cast(Literal["solaredge"], d.pop("vendor"))
        if vendor != "solaredge":
            raise ValueError(f"vendor must match const 'solaredge', got '{vendor}'")

        solaredge_join_config = cls(
            vendor=vendor,
        )

        return solaredge_join_config
