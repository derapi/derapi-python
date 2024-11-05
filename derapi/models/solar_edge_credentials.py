from typing import Any, Dict, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="SolarEdgeCredentials")


@_attrs_define
class SolarEdgeCredentials:
    """
    Attributes:
        vendor (Literal['solaredge']):  Default: 'solaredge'.
        type (Literal['apikey']):  Default: 'apikey'.
        api_key (str): SolarEdge API Key
    """

    api_key: str
    vendor: Literal["solaredge"] = "solaredge"
    type: Literal["apikey"] = "apikey"

    def to_dict(self) -> Dict[str, Any]:
        vendor = self.vendor

        type = self.type

        api_key = self.api_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "vendor": vendor,
                "type": type,
                "apiKey": api_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vendor = cast(Literal["solaredge"], d.pop("vendor"))
        if vendor != "solaredge":
            raise ValueError(f"vendor must match const 'solaredge', got '{vendor}'")

        type = cast(Literal["apikey"], d.pop("type"))
        if type != "apikey":
            raise ValueError(f"type must match const 'apikey', got '{type}'")

        api_key = d.pop("apiKey")

        solar_edge_credentials = cls(
            vendor=vendor,
            type=type,
            api_key=api_key,
        )

        return solar_edge_credentials
