import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.battery_mode import BatteryMode
from ..models.vendor import Vendor
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.battery_recent_errors_error import BatteryRecentErrorsError
    from ..models.battery_recent_errors_info import BatteryRecentErrorsInfo
    from ..models.battery_recent_errors_start import BatteryRecentErrorsStart
    from ..models.battery_recent_errors_warning import BatteryRecentErrorsWarning


T = TypeVar("T", bound="GetBatteryResponse")


@_attrs_define
class GetBatteryResponse:
    """
    Attributes:
        id (str): Battery id
        vendor (Vendor):
        reported_at (datetime.datetime): Date the request was generated in ISO-8601 format (timezone is always +00:00
            and is always present)
        model (str): Model number of Battery
        serial_number (str): Manufacturer serial number of the Battery
        site_id (str): The Derapi Site ID this Battery is associated with
        name (Union[Unset, str]): Customer defined name of the Battery
        nameplate_kwh (Union[Unset, float]): The rated storage capacity of the unit
        mode (Union[Unset, BatteryMode]): Battery management system mode. Values are Self Consumption - minimize grid
            import, Savings - optimizing Battery to save money; usually based on a rate plan, Backup - only use Battery for
            grid backup
        state_of_charge_percent (Union[Unset, float]): Battery state of charge as a percent of capacity
        recent_errors (Union[Unset, List[Union['BatteryRecentErrorsError', 'BatteryRecentErrorsInfo',
            'BatteryRecentErrorsStart', 'BatteryRecentErrorsWarning']]]): Most recent errors, warnings, or info reported by
            the manufacturer for this Battery. The key represents the severity level (info/warning/error); the value is a
            string description. start is always present and is the last element to be returned.
    """

    id: str
    vendor: Vendor
    reported_at: datetime.datetime
    model: str
    serial_number: str
    site_id: str
    name: Union[Unset, str] = UNSET
    nameplate_kwh: Union[Unset, float] = UNSET
    mode: Union[Unset, BatteryMode] = UNSET
    state_of_charge_percent: Union[Unset, float] = UNSET
    recent_errors: Union[
        Unset,
        List[
            Union[
                "BatteryRecentErrorsError",
                "BatteryRecentErrorsInfo",
                "BatteryRecentErrorsStart",
                "BatteryRecentErrorsWarning",
            ]
        ],
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.battery_recent_errors_error import BatteryRecentErrorsError
        from ..models.battery_recent_errors_info import BatteryRecentErrorsInfo
        from ..models.battery_recent_errors_warning import BatteryRecentErrorsWarning

        id = self.id

        vendor = self.vendor.value

        reported_at = self.reported_at.isoformat()

        model = self.model

        serial_number = self.serial_number

        site_id = self.site_id

        name = self.name

        nameplate_kwh = self.nameplate_kwh

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        state_of_charge_percent = self.state_of_charge_percent

        recent_errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.recent_errors, Unset):
            recent_errors = []
            for componentsschemas_battery_recent_errors_item_data in self.recent_errors:
                componentsschemas_battery_recent_errors_item: Dict[str, Any]
                if isinstance(componentsschemas_battery_recent_errors_item_data, BatteryRecentErrorsError):
                    componentsschemas_battery_recent_errors_item = (
                        componentsschemas_battery_recent_errors_item_data.to_dict()
                    )
                elif isinstance(componentsschemas_battery_recent_errors_item_data, BatteryRecentErrorsWarning):
                    componentsschemas_battery_recent_errors_item = (
                        componentsschemas_battery_recent_errors_item_data.to_dict()
                    )
                elif isinstance(componentsschemas_battery_recent_errors_item_data, BatteryRecentErrorsInfo):
                    componentsschemas_battery_recent_errors_item = (
                        componentsschemas_battery_recent_errors_item_data.to_dict()
                    )
                else:
                    componentsschemas_battery_recent_errors_item = (
                        componentsschemas_battery_recent_errors_item_data.to_dict()
                    )

                recent_errors.append(componentsschemas_battery_recent_errors_item)

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
        if nameplate_kwh is not UNSET:
            field_dict["nameplateKwh"] = nameplate_kwh
        if mode is not UNSET:
            field_dict["mode"] = mode
        if state_of_charge_percent is not UNSET:
            field_dict["stateOfChargePercent"] = state_of_charge_percent
        if recent_errors is not UNSET:
            field_dict["recentErrors"] = recent_errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.battery_recent_errors_error import BatteryRecentErrorsError
        from ..models.battery_recent_errors_info import BatteryRecentErrorsInfo
        from ..models.battery_recent_errors_start import BatteryRecentErrorsStart
        from ..models.battery_recent_errors_warning import BatteryRecentErrorsWarning

        d = src_dict.copy()
        id = d.pop("id")

        vendor = Vendor(d.pop("vendor"))

        reported_at = isoparse(d.pop("reportedAt"))

        model = d.pop("model")

        serial_number = d.pop("serialNumber")

        site_id = d.pop("siteID")

        name = d.pop("name", UNSET)

        nameplate_kwh = d.pop("nameplateKwh", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, BatteryMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = BatteryMode(_mode)

        state_of_charge_percent = d.pop("stateOfChargePercent", UNSET)

        recent_errors = []
        _recent_errors = d.pop("recentErrors", UNSET)
        for componentsschemas_battery_recent_errors_item_data in _recent_errors or []:

            def _parse_componentsschemas_battery_recent_errors_item(
                data: object,
            ) -> Union[
                "BatteryRecentErrorsError",
                "BatteryRecentErrorsInfo",
                "BatteryRecentErrorsStart",
                "BatteryRecentErrorsWarning",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_battery_recent_errors_item_type_0 = BatteryRecentErrorsError.from_dict(data)

                    return componentsschemas_battery_recent_errors_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_battery_recent_errors_item_type_1 = BatteryRecentErrorsWarning.from_dict(data)

                    return componentsschemas_battery_recent_errors_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_battery_recent_errors_item_type_2 = BatteryRecentErrorsInfo.from_dict(data)

                    return componentsschemas_battery_recent_errors_item_type_2
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_battery_recent_errors_item_type_3 = BatteryRecentErrorsStart.from_dict(data)

                return componentsschemas_battery_recent_errors_item_type_3

            componentsschemas_battery_recent_errors_item = _parse_componentsschemas_battery_recent_errors_item(
                componentsschemas_battery_recent_errors_item_data
            )

            recent_errors.append(componentsschemas_battery_recent_errors_item)

        get_battery_response = cls(
            id=id,
            vendor=vendor,
            reported_at=reported_at,
            model=model,
            serial_number=serial_number,
            site_id=site_id,
            name=name,
            nameplate_kwh=nameplate_kwh,
            mode=mode,
            state_of_charge_percent=state_of_charge_percent,
            recent_errors=recent_errors,
        )

        return get_battery_response
