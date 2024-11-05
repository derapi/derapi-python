from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.put_site_battery_control_request_interval import PutSiteBatteryControlRequestInterval


T = TypeVar("T", bound="PutSiteBatteryControlRequest")


@_attrs_define
class PutSiteBatteryControlRequest:
    """
    Attributes:
        intervals (List['PutSiteBatteryControlRequestInterval']):
    """

    intervals: List["PutSiteBatteryControlRequestInterval"]

    def to_dict(self) -> Dict[str, Any]:
        intervals = []
        for intervals_item_data in self.intervals:
            intervals_item = intervals_item_data.to_dict()
            intervals.append(intervals_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "intervals": intervals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.put_site_battery_control_request_interval import PutSiteBatteryControlRequestInterval

        d = src_dict.copy()
        intervals = []
        _intervals = d.pop("intervals")
        for intervals_item_data in _intervals:
            intervals_item = PutSiteBatteryControlRequestInterval.from_dict(intervals_item_data)

            intervals.append(intervals_item)

        put_site_battery_control_request = cls(
            intervals=intervals,
        )

        return put_site_battery_control_request
