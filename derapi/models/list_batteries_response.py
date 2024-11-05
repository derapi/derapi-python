from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.battery_summary import BatterySummary
    from ..models.list_batteries_response_errors import ListBatteriesResponseErrors


T = TypeVar("T", bound="ListBatteriesResponse")


@_attrs_define
class ListBatteriesResponse:
    """
    Attributes:
        batteries (List['BatterySummary']): List of Batteries
        errors (ListBatteriesResponseErrors): If there is an error accessing a vendor API then error details are
            provided
        next_page_token (Union[Unset, str]): A token to request the next page, if any. If absent, there are no more
            pages.
    """

    batteries: List["BatterySummary"]
    errors: "ListBatteriesResponseErrors"
    next_page_token: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        batteries = []
        for batteries_item_data in self.batteries:
            batteries_item = batteries_item_data.to_dict()
            batteries.append(batteries_item)

        errors = self.errors.to_dict()

        next_page_token = self.next_page_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "batteries": batteries,
                "errors": errors,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.battery_summary import BatterySummary
        from ..models.list_batteries_response_errors import ListBatteriesResponseErrors

        d = src_dict.copy()
        batteries = []
        _batteries = d.pop("batteries")
        for batteries_item_data in _batteries:
            batteries_item = BatterySummary.from_dict(batteries_item_data)

            batteries.append(batteries_item)

        errors = ListBatteriesResponseErrors.from_dict(d.pop("errors"))

        next_page_token = d.pop("nextPageToken", UNSET)

        list_batteries_response = cls(
            batteries=batteries,
            errors=errors,
            next_page_token=next_page_token,
        )

        return list_batteries_response
