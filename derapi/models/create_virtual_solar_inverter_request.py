import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.solar_inverter_lifetime_production import SolarInverterLifetimeProduction
    from ..models.solar_inverter_recent_production import SolarInverterRecentProduction


T = TypeVar("T", bound="CreateVirtualSolarInverterRequest")


@_attrs_define
class CreateVirtualSolarInverterRequest:
    """
    Attributes:
        site_id (Union[Unset, str]): The Derapi Site ID this Solar Inverter is associated with
        reported_at (Union[Unset, datetime.datetime]): Date the request was generated in ISO-8601 format
        model (Union[Unset, str]): Model number of this Solar Inverter
        serial_number (Union[Unset, str]): Manufacturer serial number of this Solar Inverter
        name (Union[Unset, str]): Customer defined name of this Solar Inverter
        recent_production (Union[Unset, SolarInverterRecentProduction]):
        lifetime_production (Union[Unset, SolarInverterLifetimeProduction]):
    """

    site_id: Union[Unset, str] = UNSET
    reported_at: Union[Unset, datetime.datetime] = UNSET
    model: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    recent_production: Union[Unset, "SolarInverterRecentProduction"] = UNSET
    lifetime_production: Union[Unset, "SolarInverterLifetimeProduction"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        site_id = self.site_id

        reported_at: Union[Unset, str] = UNSET
        if not isinstance(self.reported_at, Unset):
            reported_at = self.reported_at.isoformat()

        model = self.model

        serial_number = self.serial_number

        name = self.name

        recent_production: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.recent_production, Unset):
            recent_production = self.recent_production.to_dict()

        lifetime_production: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lifetime_production, Unset):
            lifetime_production = self.lifetime_production.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if site_id is not UNSET:
            field_dict["siteID"] = site_id
        if reported_at is not UNSET:
            field_dict["reportedAt"] = reported_at
        if model is not UNSET:
            field_dict["model"] = model
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if name is not UNSET:
            field_dict["name"] = name
        if recent_production is not UNSET:
            field_dict["recentProduction"] = recent_production
        if lifetime_production is not UNSET:
            field_dict["lifetimeProduction"] = lifetime_production

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.solar_inverter_lifetime_production import SolarInverterLifetimeProduction
        from ..models.solar_inverter_recent_production import SolarInverterRecentProduction

        d = src_dict.copy()
        site_id = d.pop("siteID", UNSET)

        _reported_at = d.pop("reportedAt", UNSET)
        reported_at: Union[Unset, datetime.datetime]
        if isinstance(_reported_at, Unset):
            reported_at = UNSET
        else:
            reported_at = isoparse(_reported_at)

        model = d.pop("model", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        name = d.pop("name", UNSET)

        _recent_production = d.pop("recentProduction", UNSET)
        recent_production: Union[Unset, SolarInverterRecentProduction]
        if isinstance(_recent_production, Unset):
            recent_production = UNSET
        else:
            recent_production = SolarInverterRecentProduction.from_dict(_recent_production)

        _lifetime_production = d.pop("lifetimeProduction", UNSET)
        lifetime_production: Union[Unset, SolarInverterLifetimeProduction]
        if isinstance(_lifetime_production, Unset):
            lifetime_production = UNSET
        else:
            lifetime_production = SolarInverterLifetimeProduction.from_dict(_lifetime_production)

        create_virtual_solar_inverter_request = cls(
            site_id=site_id,
            reported_at=reported_at,
            model=model,
            serial_number=serial_number,
            name=name,
            recent_production=recent_production,
            lifetime_production=lifetime_production,
        )

        return create_virtual_solar_inverter_request
