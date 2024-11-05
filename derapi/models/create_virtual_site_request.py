import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.site_location import SiteLocation


T = TypeVar("T", bound="CreateVirtualSiteRequest")


@_attrs_define
class CreateVirtualSiteRequest:
    """Fields the user would like to provide. Omitted ones will be inferred.

    Attributes:
        name (Union[Unset, str]): Customer defined name of the Site
        location (Union[Unset, SiteLocation]): The location of this Solar Inverter in lat/lon coordinates
        location_utc_offset (Union[Unset, float]): UTC Offset in hours; positive values represent locations East of UTC.
            Please note this field will soon be deprecated, please use `timezone` instead.
        operational_since (Union[Unset, datetime.datetime]): The date the Site became operational or received permission
            to operate. Sometimes absent for Solaredge.
    """

    name: Union[Unset, str] = UNSET
    location: Union[Unset, "SiteLocation"] = UNSET
    location_utc_offset: Union[Unset, float] = UNSET
    operational_since: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        location_utc_offset = self.location_utc_offset

        operational_since: Union[Unset, str] = UNSET
        if not isinstance(self.operational_since, Unset):
            operational_since = self.operational_since.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if location is not UNSET:
            field_dict["location"] = location
        if location_utc_offset is not UNSET:
            field_dict["locationUTCOffset"] = location_utc_offset
        if operational_since is not UNSET:
            field_dict["operationalSince"] = operational_since

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.site_location import SiteLocation

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, SiteLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = SiteLocation.from_dict(_location)

        location_utc_offset = d.pop("locationUTCOffset", UNSET)

        _operational_since = d.pop("operationalSince", UNSET)
        operational_since: Union[Unset, datetime.datetime]
        if isinstance(_operational_since, Unset):
            operational_since = UNSET
        else:
            operational_since = isoparse(_operational_since)

        create_virtual_site_request = cls(
            name=name,
            location=location,
            location_utc_offset=location_utc_offset,
            operational_since=operational_since,
        )

        return create_virtual_site_request
