from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteLocation")


@_attrs_define
class SiteLocation:
    """The location of this Solar Inverter in lat/lon coordinates

    Attributes:
        current_utc_offset (float): UTC Offset in (possibly fractional) hours; positive values represent locations East
            of UTC
        lat (Union[Unset, float]): Latitude coordinate of the inverter
        lon (Union[Unset, float]): Longitude coordinate of the inverter
        timezone (Union[Unset, str]): IANA timezone string
    """

    current_utc_offset: float
    lat: Union[Unset, float] = UNSET
    lon: Union[Unset, float] = UNSET
    timezone: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        current_utc_offset = self.current_utc_offset

        lat = self.lat

        lon = self.lon

        timezone = self.timezone

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "currentUTCOffset": current_utc_offset,
            }
        )
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lon is not UNSET:
            field_dict["lon"] = lon
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current_utc_offset = d.pop("currentUTCOffset")

        lat = d.pop("lat", UNSET)

        lon = d.pop("lon", UNSET)

        timezone = d.pop("timezone", UNSET)

        site_location = cls(
            current_utc_offset=current_utc_offset,
            lat=lat,
            lon=lon,
            timezone=timezone,
        )

        return site_location
