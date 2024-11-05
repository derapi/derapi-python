from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.summary_level import SummaryLevel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.battery_interval import BatteryInterval


T = TypeVar("T", bound="GetBatteryIntervalsResponse")


@_attrs_define
class GetBatteryIntervalsResponse:
    """
    Attributes:
        id (str): Battery id
        summary_level (SummaryLevel):
        intervals (List['BatteryInterval']):
        next_page_token (Union[Unset, str]): A token to request the next page, if any. If absent, there are no more
            pages.
    """

    id: str
    summary_level: SummaryLevel
    intervals: List["BatteryInterval"]
    next_page_token: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        summary_level = self.summary_level.value

        intervals = []
        for intervals_item_data in self.intervals:
            intervals_item = intervals_item_data.to_dict()
            intervals.append(intervals_item)

        next_page_token = self.next_page_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "summaryLevel": summary_level,
                "intervals": intervals,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.battery_interval import BatteryInterval

        d = src_dict.copy()
        id = d.pop("id")

        summary_level = SummaryLevel(d.pop("summaryLevel"))

        intervals = []
        _intervals = d.pop("intervals")
        for intervals_item_data in _intervals:
            intervals_item = BatteryInterval.from_dict(intervals_item_data)

            intervals.append(intervals_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        get_battery_intervals_response = cls(
            id=id,
            summary_level=summary_level,
            intervals=intervals,
            next_page_token=next_page_token,
        )

        return get_battery_intervals_response
