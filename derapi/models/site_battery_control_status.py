from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.site_battery_control_status_interval import SiteBatteryControlStatusInterval


T = TypeVar("T", bound="SiteBatteryControlStatus")


@_attrs_define
class SiteBatteryControlStatus:
    """
    Attributes:
        id (str): the ID for the Site
        intervals (List['SiteBatteryControlStatusInterval']):
    """

    id: str
    intervals: List["SiteBatteryControlStatusInterval"]

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        intervals = []
        for intervals_item_data in self.intervals:
            intervals_item = intervals_item_data.to_dict()
            intervals.append(intervals_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "intervals": intervals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.site_battery_control_status_interval import SiteBatteryControlStatusInterval

        d = src_dict.copy()
        id = d.pop("id")

        intervals = []
        _intervals = d.pop("intervals")
        for intervals_item_data in _intervals:
            intervals_item = SiteBatteryControlStatusInterval.from_dict(intervals_item_data)

            intervals.append(intervals_item)

        site_battery_control_status = cls(
            id=id,
            intervals=intervals,
        )

        return site_battery_control_status
