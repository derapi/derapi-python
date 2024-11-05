from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.virtual_battery import VirtualBattery


T = TypeVar("T", bound="ListVirtualBatteriesResponse")


@_attrs_define
class ListVirtualBatteriesResponse:
    """
    Attributes:
        virtual_batteries (List['VirtualBattery']):
        next_page_token (Union[Unset, str]): A token to request the next page, if any. If absent, there are no more
            pages.
    """

    virtual_batteries: List["VirtualBattery"]
    next_page_token: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        virtual_batteries = []
        for virtual_batteries_item_data in self.virtual_batteries:
            virtual_batteries_item = virtual_batteries_item_data.to_dict()
            virtual_batteries.append(virtual_batteries_item)

        next_page_token = self.next_page_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "virtualBatteries": virtual_batteries,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.virtual_battery import VirtualBattery

        d = src_dict.copy()
        virtual_batteries = []
        _virtual_batteries = d.pop("virtualBatteries")
        for virtual_batteries_item_data in _virtual_batteries:
            virtual_batteries_item = VirtualBattery.from_dict(virtual_batteries_item_data)

            virtual_batteries.append(virtual_batteries_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_virtual_batteries_response = cls(
            virtual_batteries=virtual_batteries,
            next_page_token=next_page_token,
        )

        return list_virtual_batteries_response
