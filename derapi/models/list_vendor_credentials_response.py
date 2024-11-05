from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vendor_credentials import VendorCredentials


T = TypeVar("T", bound="ListVendorCredentialsResponse")


@_attrs_define
class ListVendorCredentialsResponse:
    """
    Attributes:
        vendor_credentials (List['VendorCredentials']):
        next_page_token (Union[Unset, str]): A token to request the next page, if any. If absent, there are no more
            pages.
    """

    vendor_credentials: List["VendorCredentials"]
    next_page_token: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        vendor_credentials = []
        for vendor_credentials_item_data in self.vendor_credentials:
            vendor_credentials_item = vendor_credentials_item_data.to_dict()
            vendor_credentials.append(vendor_credentials_item)

        next_page_token = self.next_page_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "vendorCredentials": vendor_credentials,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.vendor_credentials import VendorCredentials

        d = src_dict.copy()
        vendor_credentials = []
        _vendor_credentials = d.pop("vendorCredentials")
        for vendor_credentials_item_data in _vendor_credentials:
            vendor_credentials_item = VendorCredentials.from_dict(vendor_credentials_item_data)

            vendor_credentials.append(vendor_credentials_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_vendor_credentials_response = cls(
            vendor_credentials=vendor_credentials,
            next_page_token=next_page_token,
        )

        return list_vendor_credentials_response
