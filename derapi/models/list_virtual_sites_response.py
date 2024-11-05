from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.virtual_site import VirtualSite


T = TypeVar("T", bound="ListVirtualSitesResponse")


@_attrs_define
class ListVirtualSitesResponse:
    """
    Attributes:
        virtual_sites (List['VirtualSite']):
        next_page_token (Union[Unset, str]): A token to request the next page, if any. If absent, there are no more
            pages.
    """

    virtual_sites: List["VirtualSite"]
    next_page_token: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        virtual_sites = []
        for virtual_sites_item_data in self.virtual_sites:
            virtual_sites_item = virtual_sites_item_data.to_dict()
            virtual_sites.append(virtual_sites_item)

        next_page_token = self.next_page_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "virtualSites": virtual_sites,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.virtual_site import VirtualSite

        d = src_dict.copy()
        virtual_sites = []
        _virtual_sites = d.pop("virtualSites")
        for virtual_sites_item_data in _virtual_sites:
            virtual_sites_item = VirtualSite.from_dict(virtual_sites_item_data)

            virtual_sites.append(virtual_sites_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_virtual_sites_response = cls(
            virtual_sites=virtual_sites,
            next_page_token=next_page_token,
        )

        return list_virtual_sites_response
