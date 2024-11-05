import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.site_battery_control_priority import SiteBatteryControlPriority
from ..models.site_battery_control_status_interval_site_battery_control_status_interval_command import (
    SiteBatteryControlStatusIntervalSiteBatteryControlStatusIntervalCommand,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteBatteryControlStatusInterval")


@_attrs_define
class SiteBatteryControlStatusInterval:
    """
    Attributes:
        command (SiteBatteryControlStatusIntervalSiteBatteryControlStatusIntervalCommand): discharge, charge, or idle
            Default: SiteBatteryControlStatusIntervalSiteBatteryControlStatusIntervalCommand.DISCHARGE.
        start (datetime.datetime): Interval start in ISO-8601 format
        end (datetime.datetime): Interval end in ISO-8601 format
        status (str): Vendor provided command status
        reported_at (datetime.datetime): The date this control status update is provided
        kw (Union[Unset, float]): discharge rate in kilowatts
        state_of_charge_limit_percent (Union[Unset, float]): the minimum/maximum state of charge, expressed as a
            percent, the Battery can be charged/discharged to
        priority (Union[Unset, SiteBatteryControlPriority]): PV = Prioritize charging the Battery with PV production or,
            for discharge, prioritize using PV production to meet Site loads first first<br /> B = Prioritize using Battery
            discharge to meet Site loads first<br /> Load = Prioritize using PV production for Sites loads first, then use
            excess to charge the Battery<br /> Grid = Prioritize charing with Battery with grid import first
        allow_export (Union[Unset, bool]): True or False
    """

    start: datetime.datetime
    end: datetime.datetime
    status: str
    reported_at: datetime.datetime
    command: SiteBatteryControlStatusIntervalSiteBatteryControlStatusIntervalCommand = (
        SiteBatteryControlStatusIntervalSiteBatteryControlStatusIntervalCommand.DISCHARGE
    )
    kw: Union[Unset, float] = UNSET
    state_of_charge_limit_percent: Union[Unset, float] = UNSET
    priority: Union[Unset, SiteBatteryControlPriority] = UNSET
    allow_export: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        command = self.command.value

        start = self.start.isoformat()

        end = self.end.isoformat()

        status = self.status

        reported_at = self.reported_at.isoformat()

        kw = self.kw

        state_of_charge_limit_percent = self.state_of_charge_limit_percent

        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        allow_export = self.allow_export

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "command": command,
                "start": start,
                "end": end,
                "status": status,
                "reportedAt": reported_at,
            }
        )
        if kw is not UNSET:
            field_dict["kw"] = kw
        if state_of_charge_limit_percent is not UNSET:
            field_dict["stateOfChargeLimitPercent"] = state_of_charge_limit_percent
        if priority is not UNSET:
            field_dict["priority"] = priority
        if allow_export is not UNSET:
            field_dict["allowExport"] = allow_export

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        command = SiteBatteryControlStatusIntervalSiteBatteryControlStatusIntervalCommand(d.pop("command"))

        start = isoparse(d.pop("start"))

        end = isoparse(d.pop("end"))

        status = d.pop("status")

        reported_at = isoparse(d.pop("reportedAt"))

        kw = d.pop("kw", UNSET)

        state_of_charge_limit_percent = d.pop("stateOfChargeLimitPercent", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, SiteBatteryControlPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = SiteBatteryControlPriority(_priority)

        allow_export = d.pop("allowExport", UNSET)

        site_battery_control_status_interval = cls(
            command=command,
            start=start,
            end=end,
            status=status,
            reported_at=reported_at,
            kw=kw,
            state_of_charge_limit_percent=state_of_charge_limit_percent,
            priority=priority,
            allow_export=allow_export,
        )

        return site_battery_control_status_interval
