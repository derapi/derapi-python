import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.vendor import Vendor
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.solar_inverter_lifetime_production import SolarInverterLifetimeProduction
    from ..models.solar_inverter_recent_errors_error import SolarInverterRecentErrorsError
    from ..models.solar_inverter_recent_errors_info import SolarInverterRecentErrorsInfo
    from ..models.solar_inverter_recent_errors_start import SolarInverterRecentErrorsStart
    from ..models.solar_inverter_recent_errors_warning import SolarInverterRecentErrorsWarning
    from ..models.solar_inverter_recent_production import SolarInverterRecentProduction


T = TypeVar("T", bound="CreateVirtualSolarInverterResponse")


@_attrs_define
class CreateVirtualSolarInverterResponse:
    """
    Attributes:
        id (str): ID of the solar inverter
        vendor (Vendor):
        reported_at (datetime.datetime): Date the request was generated in ISO-8601 format
        model (str): Model number of this Solar Inverter
        serial_number (str): Manufacturer serial number of this Solar Inverter
        site_id (str): The Derapi Site ID this Solar Inverter is associated with
        name (Union[Unset, str]): Customer defined name of this Solar Inverter
        recent_production (Union[Unset, SolarInverterRecentProduction]):
        lifetime_production (Union[Unset, SolarInverterLifetimeProduction]):
        recent_errors (Union[Unset, List[Union['SolarInverterRecentErrorsError', 'SolarInverterRecentErrorsInfo',
            'SolarInverterRecentErrorsStart', 'SolarInverterRecentErrorsWarning']]]): Most recent errors, warnings, or info
            reported by the manufacturer for this Solar Inverter. The key represents the severity level
            (info/warning/error); the value is a string description. start is always present and is the last element to be
            returned.
    """

    id: str
    vendor: Vendor
    reported_at: datetime.datetime
    model: str
    serial_number: str
    site_id: str
    name: Union[Unset, str] = UNSET
    recent_production: Union[Unset, "SolarInverterRecentProduction"] = UNSET
    lifetime_production: Union[Unset, "SolarInverterLifetimeProduction"] = UNSET
    recent_errors: Union[
        Unset,
        List[
            Union[
                "SolarInverterRecentErrorsError",
                "SolarInverterRecentErrorsInfo",
                "SolarInverterRecentErrorsStart",
                "SolarInverterRecentErrorsWarning",
            ]
        ],
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.solar_inverter_recent_errors_error import SolarInverterRecentErrorsError
        from ..models.solar_inverter_recent_errors_info import SolarInverterRecentErrorsInfo
        from ..models.solar_inverter_recent_errors_warning import SolarInverterRecentErrorsWarning

        id = self.id

        vendor = self.vendor.value

        reported_at = self.reported_at.isoformat()

        model = self.model

        serial_number = self.serial_number

        site_id = self.site_id

        name = self.name

        recent_production: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.recent_production, Unset):
            recent_production = self.recent_production.to_dict()

        lifetime_production: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lifetime_production, Unset):
            lifetime_production = self.lifetime_production.to_dict()

        recent_errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.recent_errors, Unset):
            recent_errors = []
            for componentsschemas_solar_inverter_recent_errors_item_data in self.recent_errors:
                componentsschemas_solar_inverter_recent_errors_item: Dict[str, Any]
                if isinstance(componentsschemas_solar_inverter_recent_errors_item_data, SolarInverterRecentErrorsError):
                    componentsschemas_solar_inverter_recent_errors_item = (
                        componentsschemas_solar_inverter_recent_errors_item_data.to_dict()
                    )
                elif isinstance(
                    componentsschemas_solar_inverter_recent_errors_item_data, SolarInverterRecentErrorsWarning
                ):
                    componentsschemas_solar_inverter_recent_errors_item = (
                        componentsschemas_solar_inverter_recent_errors_item_data.to_dict()
                    )
                elif isinstance(
                    componentsschemas_solar_inverter_recent_errors_item_data, SolarInverterRecentErrorsInfo
                ):
                    componentsschemas_solar_inverter_recent_errors_item = (
                        componentsschemas_solar_inverter_recent_errors_item_data.to_dict()
                    )
                else:
                    componentsschemas_solar_inverter_recent_errors_item = (
                        componentsschemas_solar_inverter_recent_errors_item_data.to_dict()
                    )

                recent_errors.append(componentsschemas_solar_inverter_recent_errors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "vendor": vendor,
                "reportedAt": reported_at,
                "model": model,
                "serialNumber": serial_number,
                "siteID": site_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if recent_production is not UNSET:
            field_dict["recentProduction"] = recent_production
        if lifetime_production is not UNSET:
            field_dict["lifetimeProduction"] = lifetime_production
        if recent_errors is not UNSET:
            field_dict["recentErrors"] = recent_errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.solar_inverter_lifetime_production import SolarInverterLifetimeProduction
        from ..models.solar_inverter_recent_errors_error import SolarInverterRecentErrorsError
        from ..models.solar_inverter_recent_errors_info import SolarInverterRecentErrorsInfo
        from ..models.solar_inverter_recent_errors_start import SolarInverterRecentErrorsStart
        from ..models.solar_inverter_recent_errors_warning import SolarInverterRecentErrorsWarning
        from ..models.solar_inverter_recent_production import SolarInverterRecentProduction

        d = src_dict.copy()
        id = d.pop("id")

        vendor = Vendor(d.pop("vendor"))

        reported_at = isoparse(d.pop("reportedAt"))

        model = d.pop("model")

        serial_number = d.pop("serialNumber")

        site_id = d.pop("siteID")

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

        recent_errors = []
        _recent_errors = d.pop("recentErrors", UNSET)
        for componentsschemas_solar_inverter_recent_errors_item_data in _recent_errors or []:

            def _parse_componentsschemas_solar_inverter_recent_errors_item(
                data: object,
            ) -> Union[
                "SolarInverterRecentErrorsError",
                "SolarInverterRecentErrorsInfo",
                "SolarInverterRecentErrorsStart",
                "SolarInverterRecentErrorsWarning",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_solar_inverter_recent_errors_item_type_0 = (
                        SolarInverterRecentErrorsError.from_dict(data)
                    )

                    return componentsschemas_solar_inverter_recent_errors_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_solar_inverter_recent_errors_item_type_1 = (
                        SolarInverterRecentErrorsWarning.from_dict(data)
                    )

                    return componentsschemas_solar_inverter_recent_errors_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_solar_inverter_recent_errors_item_type_2 = (
                        SolarInverterRecentErrorsInfo.from_dict(data)
                    )

                    return componentsschemas_solar_inverter_recent_errors_item_type_2
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_solar_inverter_recent_errors_item_type_3 = SolarInverterRecentErrorsStart.from_dict(
                    data
                )

                return componentsschemas_solar_inverter_recent_errors_item_type_3

            componentsschemas_solar_inverter_recent_errors_item = (
                _parse_componentsschemas_solar_inverter_recent_errors_item(
                    componentsschemas_solar_inverter_recent_errors_item_data
                )
            )

            recent_errors.append(componentsschemas_solar_inverter_recent_errors_item)

        create_virtual_solar_inverter_response = cls(
            id=id,
            vendor=vendor,
            reported_at=reported_at,
            model=model,
            serial_number=serial_number,
            site_id=site_id,
            name=name,
            recent_production=recent_production,
            lifetime_production=lifetime_production,
            recent_errors=recent_errors,
        )

        return create_virtual_solar_inverter_response
