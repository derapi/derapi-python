from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_site_response_errors import ListSiteResponseErrors
    from ..models.site_summary import SiteSummary


T = TypeVar("T", bound="ListSitesResponse")


@_attrs_define
class ListSitesResponse:
    """
    Attributes:
        sites (List['SiteSummary']): List of Sites
        errors (ListSiteResponseErrors): If there is an error accessing a vendor API then error details are provided
        next_page_token (Union[Unset, str]): A token to request the next page, if any. If absent, there are no more
            pages.
    """

    sites: List["SiteSummary"]
    errors: "ListSiteResponseErrors"
    next_page_token: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        sites = []
        for sites_item_data in self.sites:
            sites_item = sites_item_data.to_dict()
            sites.append(sites_item)

        errors = self.errors.to_dict()

        next_page_token = self.next_page_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "sites": sites,
                "errors": errors,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_site_response_errors import ListSiteResponseErrors
        from ..models.site_summary import SiteSummary

        d = src_dict.copy()
        sites = []
        _sites = d.pop("sites")
        for sites_item_data in _sites:
            sites_item = SiteSummary.from_dict(sites_item_data)

            sites.append(sites_item)

        errors = ListSiteResponseErrors.from_dict(d.pop("errors"))

        next_page_token = d.pop("nextPageToken", UNSET)

        list_sites_response = cls(
            sites=sites,
            errors=errors,
            next_page_token=next_page_token,
        )

        return list_sites_response
