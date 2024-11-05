from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.enphase_developer_app_credentials import EnphaseDeveloperAppCredentials
    from ..models.enphase_partner_app_credentials import EnphasePartnerAppCredentials
    from ..models.enphase_vpp_credentials import EnphaseVPPCredentials
    from ..models.franklin_wh_credentials import FranklinWHCredentials
    from ..models.sma_custom_grant_credentials import SMACustomGrantCredentials
    from ..models.sma_sandbox_custom_grant_credentials import SMASandboxCustomGrantCredentials
    from ..models.sma_sandbox_o_auth_credentials import SMASandboxOAuthCredentials
    from ..models.smao_auth_credentials import SMAOAuthCredentials
    from ..models.solar_edge_credentials import SolarEdgeCredentials
    from ..models.solis_credentials import SolisCredentials
    from ..models.tesla_app_credentials import TeslaAppCredentials


T = TypeVar("T", bound="UpdateVendorCredentialsRequest")


@_attrs_define
class UpdateVendorCredentialsRequest:
    """
    Attributes:
        name (Union[None, Unset, str]): The name of the vendor credentials; if null, the value will be unset.
        credentials (Union['EnphaseDeveloperAppCredentials', 'EnphasePartnerAppCredentials', 'EnphaseVPPCredentials',
            'FranklinWHCredentials', 'SMACustomGrantCredentials', 'SMAOAuthCredentials', 'SMASandboxCustomGrantCredentials',
            'SMASandboxOAuthCredentials', 'SolarEdgeCredentials', 'SolisCredentials', 'TeslaAppCredentials', Unset]):
            Credentials for a given vendor.
    """

    name: Union[None, Unset, str] = UNSET
    credentials: Union[
        "EnphaseDeveloperAppCredentials",
        "EnphasePartnerAppCredentials",
        "EnphaseVPPCredentials",
        "FranklinWHCredentials",
        "SMACustomGrantCredentials",
        "SMAOAuthCredentials",
        "SMASandboxCustomGrantCredentials",
        "SMASandboxOAuthCredentials",
        "SolarEdgeCredentials",
        "SolisCredentials",
        "TeslaAppCredentials",
        Unset,
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.enphase_developer_app_credentials import EnphaseDeveloperAppCredentials
        from ..models.enphase_partner_app_credentials import EnphasePartnerAppCredentials
        from ..models.enphase_vpp_credentials import EnphaseVPPCredentials
        from ..models.franklin_wh_credentials import FranklinWHCredentials
        from ..models.sma_custom_grant_credentials import SMACustomGrantCredentials
        from ..models.sma_sandbox_custom_grant_credentials import SMASandboxCustomGrantCredentials
        from ..models.sma_sandbox_o_auth_credentials import SMASandboxOAuthCredentials
        from ..models.smao_auth_credentials import SMAOAuthCredentials
        from ..models.solar_edge_credentials import SolarEdgeCredentials
        from ..models.solis_credentials import SolisCredentials

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        credentials: Union[Dict[str, Any], Unset]
        if isinstance(self.credentials, Unset):
            credentials = UNSET
        elif isinstance(self.credentials, EnphasePartnerAppCredentials):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, EnphaseDeveloperAppCredentials):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, EnphaseVPPCredentials):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, FranklinWHCredentials):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, SMACustomGrantCredentials):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, SMAOAuthCredentials):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, SMASandboxCustomGrantCredentials):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, SMASandboxOAuthCredentials):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, SolarEdgeCredentials):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, SolisCredentials):
            credentials = self.credentials.to_dict()
        else:
            credentials = self.credentials.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if credentials is not UNSET:
            field_dict["credentials"] = credentials

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.enphase_developer_app_credentials import EnphaseDeveloperAppCredentials
        from ..models.enphase_partner_app_credentials import EnphasePartnerAppCredentials
        from ..models.enphase_vpp_credentials import EnphaseVPPCredentials
        from ..models.franklin_wh_credentials import FranklinWHCredentials
        from ..models.sma_custom_grant_credentials import SMACustomGrantCredentials
        from ..models.sma_sandbox_custom_grant_credentials import SMASandboxCustomGrantCredentials
        from ..models.sma_sandbox_o_auth_credentials import SMASandboxOAuthCredentials
        from ..models.smao_auth_credentials import SMAOAuthCredentials
        from ..models.solar_edge_credentials import SolarEdgeCredentials
        from ..models.solis_credentials import SolisCredentials
        from ..models.tesla_app_credentials import TeslaAppCredentials

        d = src_dict.copy()

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_credentials(
            data: object,
        ) -> Union[
            "EnphaseDeveloperAppCredentials",
            "EnphasePartnerAppCredentials",
            "EnphaseVPPCredentials",
            "FranklinWHCredentials",
            "SMACustomGrantCredentials",
            "SMAOAuthCredentials",
            "SMASandboxCustomGrantCredentials",
            "SMASandboxOAuthCredentials",
            "SolarEdgeCredentials",
            "SolisCredentials",
            "TeslaAppCredentials",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_vendor_credentials_credentials_type_0 = EnphasePartnerAppCredentials.from_dict(data)

                return componentsschemas_vendor_credentials_credentials_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_vendor_credentials_credentials_type_1 = EnphaseDeveloperAppCredentials.from_dict(data)

                return componentsschemas_vendor_credentials_credentials_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_vendor_credentials_credentials_type_2 = EnphaseVPPCredentials.from_dict(data)

                return componentsschemas_vendor_credentials_credentials_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_vendor_credentials_credentials_type_3 = FranklinWHCredentials.from_dict(data)

                return componentsschemas_vendor_credentials_credentials_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_vendor_credentials_credentials_type_4 = SMACustomGrantCredentials.from_dict(data)

                return componentsschemas_vendor_credentials_credentials_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_vendor_credentials_credentials_type_5 = SMAOAuthCredentials.from_dict(data)

                return componentsschemas_vendor_credentials_credentials_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_vendor_credentials_credentials_type_6 = SMASandboxCustomGrantCredentials.from_dict(
                    data
                )

                return componentsschemas_vendor_credentials_credentials_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_vendor_credentials_credentials_type_7 = SMASandboxOAuthCredentials.from_dict(data)

                return componentsschemas_vendor_credentials_credentials_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_vendor_credentials_credentials_type_8 = SolarEdgeCredentials.from_dict(data)

                return componentsschemas_vendor_credentials_credentials_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_vendor_credentials_credentials_type_9 = SolisCredentials.from_dict(data)

                return componentsschemas_vendor_credentials_credentials_type_9
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_vendor_credentials_credentials_type_10 = TeslaAppCredentials.from_dict(data)

            return componentsschemas_vendor_credentials_credentials_type_10

        credentials = _parse_credentials(d.pop("credentials", UNSET))

        update_vendor_credentials_request = cls(
            name=name,
            credentials=credentials,
        )

        return update_vendor_credentials_request
