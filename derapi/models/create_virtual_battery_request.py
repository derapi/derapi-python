import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.battery_mode import BatteryMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateVirtualBatteryRequest")


@_attrs_define
class CreateVirtualBatteryRequest:
    """Fields the user would like to provide. Omitted ones will be inferred.

    Attributes:
        name (Union[Unset, str]): Customer defined name of the Battery
        site_id (Union[Unset, str]): The Derapi Site ID this Battery is associated with
        reported_at (Union[Unset, datetime.datetime]): Date the request was generated in ISO-8601 format (timezone is
            always +00:00 and is always present)
        model (Union[Unset, str]): Model number of Battery
        serial_number (Union[Unset, str]): Manufacturer serial number of the Battery
        nameplate_kwh (Union[Unset, float]): The rated storage capacity of the unit
        mode (Union[Unset, BatteryMode]): Battery management system mode. Values are Self Consumption - minimize grid
            import, Savings - optimizing Battery to save money; usually based on a rate plan, Backup - only use Battery for
            grid backup
        state_of_charge_percent (Union[Unset, float]): Battery state of charge as a percent of capacity
    """

    name: Union[Unset, str] = UNSET
    site_id: Union[Unset, str] = UNSET
    reported_at: Union[Unset, datetime.datetime] = UNSET
    model: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    nameplate_kwh: Union[Unset, float] = UNSET
    mode: Union[Unset, BatteryMode] = UNSET
    state_of_charge_percent: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        site_id = self.site_id

        reported_at: Union[Unset, str] = UNSET
        if not isinstance(self.reported_at, Unset):
            reported_at = self.reported_at.isoformat()

        model = self.model

        serial_number = self.serial_number

        nameplate_kwh = self.nameplate_kwh

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        state_of_charge_percent = self.state_of_charge_percent

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if site_id is not UNSET:
            field_dict["siteID"] = site_id
        if reported_at is not UNSET:
            field_dict["reportedAt"] = reported_at
        if model is not UNSET:
            field_dict["model"] = model
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if nameplate_kwh is not UNSET:
            field_dict["nameplateKwh"] = nameplate_kwh
        if mode is not UNSET:
            field_dict["mode"] = mode
        if state_of_charge_percent is not UNSET:
            field_dict["stateOfChargePercent"] = state_of_charge_percent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        site_id = d.pop("siteID", UNSET)

        _reported_at = d.pop("reportedAt", UNSET)
        reported_at: Union[Unset, datetime.datetime]
        if isinstance(_reported_at, Unset):
            reported_at = UNSET
        else:
            reported_at = isoparse(_reported_at)

        model = d.pop("model", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        nameplate_kwh = d.pop("nameplateKwh", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, BatteryMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = BatteryMode(_mode)

        state_of_charge_percent = d.pop("stateOfChargePercent", UNSET)

        create_virtual_battery_request = cls(
            name=name,
            site_id=site_id,
            reported_at=reported_at,
            model=model,
            serial_number=serial_number,
            nameplate_kwh=nameplate_kwh,
            mode=mode,
            state_of_charge_percent=state_of_charge_percent,
        )

        return create_virtual_battery_request
