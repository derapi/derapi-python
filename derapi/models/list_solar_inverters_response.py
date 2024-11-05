from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_solar_inverters_response_errors import ListSolarInvertersResponseErrors
    from ..models.solar_inverter_summary import SolarInverterSummary


T = TypeVar("T", bound="ListSolarInvertersResponse")


@_attrs_define
class ListSolarInvertersResponse:
    """
    Attributes:
        solar_inverters (List['SolarInverterSummary']): List of Solar Inverters
        errors (ListSolarInvertersResponseErrors): If there is an error accessing a vendor API then error details are
            provided
        next_page_token (Union[Unset, str]): A token to request the next page, if any. If absent, there are no more
            pages.
    """

    solar_inverters: List["SolarInverterSummary"]
    errors: "ListSolarInvertersResponseErrors"
    next_page_token: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        solar_inverters = []
        for solar_inverters_item_data in self.solar_inverters:
            solar_inverters_item = solar_inverters_item_data.to_dict()
            solar_inverters.append(solar_inverters_item)

        errors = self.errors.to_dict()

        next_page_token = self.next_page_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "solarInverters": solar_inverters,
                "errors": errors,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_solar_inverters_response_errors import ListSolarInvertersResponseErrors
        from ..models.solar_inverter_summary import SolarInverterSummary

        d = src_dict.copy()
        solar_inverters = []
        _solar_inverters = d.pop("solarInverters")
        for solar_inverters_item_data in _solar_inverters:
            solar_inverters_item = SolarInverterSummary.from_dict(solar_inverters_item_data)

            solar_inverters.append(solar_inverters_item)

        errors = ListSolarInvertersResponseErrors.from_dict(d.pop("errors"))

        next_page_token = d.pop("nextPageToken", UNSET)

        list_solar_inverters_response = cls(
            solar_inverters=solar_inverters,
            errors=errors,
            next_page_token=next_page_token,
        )

        return list_solar_inverters_response
