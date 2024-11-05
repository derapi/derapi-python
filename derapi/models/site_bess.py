from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteBESS")


@_attrs_define
class SiteBESS:
    """For Sites with Batteries this key is present

    Attributes:
        nameplate_kwh (Union[Unset, float]): The rated storage capacity of the system in kWh
        mode (Union[Unset, str]): Battery management system mode
        state_of_charge_percent (Union[Unset, float]): Battery system state of charge as a percent of capacity
    """

    nameplate_kwh: Union[Unset, float] = UNSET
    mode: Union[Unset, str] = UNSET
    state_of_charge_percent: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        nameplate_kwh = self.nameplate_kwh

        mode = self.mode

        state_of_charge_percent = self.state_of_charge_percent

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
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
        nameplate_kwh = d.pop("nameplateKwh", UNSET)

        mode = d.pop("mode", UNSET)

        state_of_charge_percent = d.pop("stateOfChargePercent", UNSET)

        site_bess = cls(
            nameplate_kwh=nameplate_kwh,
            mode=mode,
            state_of_charge_percent=state_of_charge_percent,
        )

        return site_bess
