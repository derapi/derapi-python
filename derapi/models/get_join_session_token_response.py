from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetJoinSessionTokenResponse")


@_attrs_define
class GetJoinSessionTokenResponse:
    """
    Attributes:
        vendor (str): The vendor that the client authorized (sma, enphase, solis, solaredge, enphasevpp, tesla)
        access_token (str): The public access token to use when requesting data for clients system
        refresh_token (str): The refresh token to use when requesting a new token for clients system
        expires_in (str): Amount of time the accessToken is valid (in seconds)
        site_id (Union[Unset, str]): Only for enphasevpp, the siteID for the clients system
    """

    vendor: str
    access_token: str
    refresh_token: str
    expires_in: str
    site_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        vendor = self.vendor

        access_token = self.access_token

        refresh_token = self.refresh_token

        expires_in = self.expires_in

        site_id = self.site_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "vendor": vendor,
                "accessToken": access_token,
                "refreshToken": refresh_token,
                "expiresIn": expires_in,
            }
        )
        if site_id is not UNSET:
            field_dict["siteID"] = site_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vendor = d.pop("vendor")

        access_token = d.pop("accessToken")

        refresh_token = d.pop("refreshToken")

        expires_in = d.pop("expiresIn")

        site_id = d.pop("siteID", UNSET)

        get_join_session_token_response = cls(
            vendor=vendor,
            access_token=access_token,
            refresh_token=refresh_token,
            expires_in=expires_in,
            site_id=site_id,
        )

        return get_join_session_token_response
