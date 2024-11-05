from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.virtual_solar_inverter import VirtualSolarInverter


T = TypeVar("T", bound="ListVirtualSolarInvertersResponse")


@_attrs_define
class ListVirtualSolarInvertersResponse:
    """
    Attributes:
        virtual_solar_inverters (List['VirtualSolarInverter']):
        next_page_token (Union[Unset, str]): A token to request the next page, if any. If absent, there are no more
            pages.
    """

    virtual_solar_inverters: List["VirtualSolarInverter"]
    next_page_token: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        virtual_solar_inverters = []
        for virtual_solar_inverters_item_data in self.virtual_solar_inverters:
            virtual_solar_inverters_item = virtual_solar_inverters_item_data.to_dict()
            virtual_solar_inverters.append(virtual_solar_inverters_item)

        next_page_token = self.next_page_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "virtualSolarInverters": virtual_solar_inverters,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.virtual_solar_inverter import VirtualSolarInverter

        d = src_dict.copy()
        virtual_solar_inverters = []
        _virtual_solar_inverters = d.pop("virtualSolarInverters")
        for virtual_solar_inverters_item_data in _virtual_solar_inverters:
            virtual_solar_inverters_item = VirtualSolarInverter.from_dict(virtual_solar_inverters_item_data)

            virtual_solar_inverters.append(virtual_solar_inverters_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_virtual_solar_inverters_response = cls(
            virtual_solar_inverters=virtual_solar_inverters,
            next_page_token=next_page_token,
        )

        return list_virtual_solar_inverters_response
