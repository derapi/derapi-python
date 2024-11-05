import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.vendor import Vendor
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.battery_summary import BatterySummary
    from ..models.site_bess import SiteBESS
    from ..models.site_location import SiteLocation
    from ..models.solar_inverter_summary import SolarInverterSummary


T = TypeVar("T", bound="CreateVirtualSiteResponse")


@_attrs_define
class CreateVirtualSiteResponse:
    """
    Attributes:
        id (str): the ID for the Site
        vendor (Vendor):
        name (str): Customer defined name of the Site
        location_utc_offset (float): UTC Offset in hours; positive values represent locations East of UTC. Please note
            this field will soon be deprecated, please use `timezone` instead.
        batteries (List['BatterySummary']): List of Battery IDs associated with this Site
        solar_inverters (List['SolarInverterSummary']): List of Solar Inverter IDs associated with this Site
        location (Union[Unset, SiteLocation]): The location of this Solar Inverter in lat/lon coordinates
        operational_since (Union[Unset, datetime.datetime]): The date the Site became operational or received permission
            to operate. Sometimes absent for Solaredge.
        bess (Union[Unset, SiteBESS]): For Sites with Batteries this key is present
    """

    id: str
    vendor: Vendor
    name: str
    location_utc_offset: float
    batteries: List["BatterySummary"]
    solar_inverters: List["SolarInverterSummary"]
    location: Union[Unset, "SiteLocation"] = UNSET
    operational_since: Union[Unset, datetime.datetime] = UNSET
    bess: Union[Unset, "SiteBESS"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        vendor = self.vendor.value

        name = self.name

        location_utc_offset = self.location_utc_offset

        batteries = []
        for componentsschemas_site_batteries_item_data in self.batteries:
            componentsschemas_site_batteries_item = componentsschemas_site_batteries_item_data.to_dict()
            batteries.append(componentsschemas_site_batteries_item)

        solar_inverters = []
        for componentsschemas_site_solar_inverters_item_data in self.solar_inverters:
            componentsschemas_site_solar_inverters_item = componentsschemas_site_solar_inverters_item_data.to_dict()
            solar_inverters.append(componentsschemas_site_solar_inverters_item)

        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        operational_since: Union[Unset, str] = UNSET
        if not isinstance(self.operational_since, Unset):
            operational_since = self.operational_since.isoformat()

        bess: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bess, Unset):
            bess = self.bess.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "vendor": vendor,
                "name": name,
                "locationUTCOffset": location_utc_offset,
                "batteries": batteries,
                "solarInverters": solar_inverters,
            }
        )
        if location is not UNSET:
            field_dict["location"] = location
        if operational_since is not UNSET:
            field_dict["operationalSince"] = operational_since
        if bess is not UNSET:
            field_dict["bess"] = bess

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.battery_summary import BatterySummary
        from ..models.site_bess import SiteBESS
        from ..models.site_location import SiteLocation
        from ..models.solar_inverter_summary import SolarInverterSummary

        d = src_dict.copy()
        id = d.pop("id")

        vendor = Vendor(d.pop("vendor"))

        name = d.pop("name")

        location_utc_offset = d.pop("locationUTCOffset")

        batteries = []
        _batteries = d.pop("batteries")
        for componentsschemas_site_batteries_item_data in _batteries:
            componentsschemas_site_batteries_item = BatterySummary.from_dict(componentsschemas_site_batteries_item_data)

            batteries.append(componentsschemas_site_batteries_item)

        solar_inverters = []
        _solar_inverters = d.pop("solarInverters")
        for componentsschemas_site_solar_inverters_item_data in _solar_inverters:
            componentsschemas_site_solar_inverters_item = SolarInverterSummary.from_dict(
                componentsschemas_site_solar_inverters_item_data
            )

            solar_inverters.append(componentsschemas_site_solar_inverters_item)

        _location = d.pop("location", UNSET)
        location: Union[Unset, SiteLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = SiteLocation.from_dict(_location)

        _operational_since = d.pop("operationalSince", UNSET)
        operational_since: Union[Unset, datetime.datetime]
        if isinstance(_operational_since, Unset):
            operational_since = UNSET
        else:
            operational_since = isoparse(_operational_since)

        _bess = d.pop("bess", UNSET)
        bess: Union[Unset, SiteBESS]
        if isinstance(_bess, Unset):
            bess = UNSET
        else:
            bess = SiteBESS.from_dict(_bess)

        create_virtual_site_response = cls(
            id=id,
            vendor=vendor,
            name=name,
            location_utc_offset=location_utc_offset,
            batteries=batteries,
            solar_inverters=solar_inverters,
            location=location,
            operational_since=operational_since,
            bess=bess,
        )

        return create_virtual_site_response
