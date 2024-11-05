from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.enphase_developer_app_credentials import EnphaseDeveloperAppCredentials
    from ..models.enphase_partner_app_credentials import EnphasePartnerAppCredentials
    from ..models.enphase_vpp_credentials import EnphaseVPPCredentials
    from ..models.franklin_wh_credentials import FranklinWHCredentials
    from ..models.hidden_enphase_developer_app_credentials import HiddenEnphaseDeveloperAppCredentials
    from ..models.hidden_enphase_partner_app_credentials import HiddenEnphasePartnerAppCredentials
    from ..models.hidden_enphase_vpp_credentials import HiddenEnphaseVPPCredentials
    from ..models.hidden_franklin_wh_credentials import HiddenFranklinWHCredentials
    from ..models.hidden_sma_custom_grant_credentials import HiddenSMACustomGrantCredentials
    from ..models.hidden_sma_sandbox_custom_grant_credentials import HiddenSMASandboxCustomGrantCredentials
    from ..models.hidden_sma_sandbox_o_auth_credentials import HiddenSMASandboxOAuthCredentials
    from ..models.hidden_smao_auth_credentials import HiddenSMAOAuthCredentials
    from ..models.hidden_solar_edge_credentials import HiddenSolarEdgeCredentials
    from ..models.hidden_solis_credentials import HiddenSolisCredentials
    from ..models.hidden_tesla_app_credentials import HiddenTeslaAppCredentials
    from ..models.sma_custom_grant_credentials import SMACustomGrantCredentials
    from ..models.sma_sandbox_custom_grant_credentials import SMASandboxCustomGrantCredentials
    from ..models.sma_sandbox_o_auth_credentials import SMASandboxOAuthCredentials
    from ..models.smao_auth_credentials import SMAOAuthCredentials
    from ..models.solar_edge_credentials import SolarEdgeCredentials
    from ..models.solis_credentials import SolisCredentials
    from ..models.tesla_app_credentials import TeslaAppCredentials


T = TypeVar("T", bound="UpdateVendorCredentialsResponse")


@_attrs_define
class UpdateVendorCredentialsResponse:
    """Vendor credentials which may or may not be hidden.

    Attributes:
        id (str): ID for the vendor credentials
        name (str): The name of the vendor credentials; inferred if not provided.
        credentials (Union['EnphaseDeveloperAppCredentials', 'EnphasePartnerAppCredentials', 'EnphaseVPPCredentials',
            'FranklinWHCredentials', 'HiddenEnphaseDeveloperAppCredentials', 'HiddenEnphasePartnerAppCredentials',
            'HiddenEnphaseVPPCredentials', 'HiddenFranklinWHCredentials', 'HiddenSMACustomGrantCredentials',
            'HiddenSMAOAuthCredentials', 'HiddenSMASandboxCustomGrantCredentials', 'HiddenSMASandboxOAuthCredentials',
            'HiddenSolarEdgeCredentials', 'HiddenSolisCredentials', 'HiddenTeslaAppCredentials',
            'SMACustomGrantCredentials', 'SMAOAuthCredentials', 'SMASandboxCustomGrantCredentials',
            'SMASandboxOAuthCredentials', 'SolarEdgeCredentials', 'SolisCredentials', 'TeslaAppCredentials']):
    """

    id: str
    name: str
    credentials: Union[
        "EnphaseDeveloperAppCredentials",
        "EnphasePartnerAppCredentials",
        "EnphaseVPPCredentials",
        "FranklinWHCredentials",
        "HiddenEnphaseDeveloperAppCredentials",
        "HiddenEnphasePartnerAppCredentials",
        "HiddenEnphaseVPPCredentials",
        "HiddenFranklinWHCredentials",
        "HiddenSMACustomGrantCredentials",
        "HiddenSMAOAuthCredentials",
        "HiddenSMASandboxCustomGrantCredentials",
        "HiddenSMASandboxOAuthCredentials",
        "HiddenSolarEdgeCredentials",
        "HiddenSolisCredentials",
        "HiddenTeslaAppCredentials",
        "SMACustomGrantCredentials",
        "SMAOAuthCredentials",
        "SMASandboxCustomGrantCredentials",
        "SMASandboxOAuthCredentials",
        "SolarEdgeCredentials",
        "SolisCredentials",
        "TeslaAppCredentials",
    ]

    def to_dict(self) -> Dict[str, Any]:
        from ..models.enphase_developer_app_credentials import EnphaseDeveloperAppCredentials
        from ..models.enphase_partner_app_credentials import EnphasePartnerAppCredentials
        from ..models.enphase_vpp_credentials import EnphaseVPPCredentials
        from ..models.franklin_wh_credentials import FranklinWHCredentials
        from ..models.hidden_enphase_developer_app_credentials import HiddenEnphaseDeveloperAppCredentials
        from ..models.hidden_enphase_partner_app_credentials import HiddenEnphasePartnerAppCredentials
        from ..models.hidden_enphase_vpp_credentials import HiddenEnphaseVPPCredentials
        from ..models.hidden_franklin_wh_credentials import HiddenFranklinWHCredentials
        from ..models.hidden_sma_custom_grant_credentials import HiddenSMACustomGrantCredentials
        from ..models.hidden_sma_sandbox_custom_grant_credentials import HiddenSMASandboxCustomGrantCredentials
        from ..models.hidden_sma_sandbox_o_auth_credentials import HiddenSMASandboxOAuthCredentials
        from ..models.hidden_smao_auth_credentials import HiddenSMAOAuthCredentials
        from ..models.hidden_solar_edge_credentials import HiddenSolarEdgeCredentials
        from ..models.hidden_solis_credentials import HiddenSolisCredentials
        from ..models.hidden_tesla_app_credentials import HiddenTeslaAppCredentials
        from ..models.sma_custom_grant_credentials import SMACustomGrantCredentials
        from ..models.sma_sandbox_custom_grant_credentials import SMASandboxCustomGrantCredentials
        from ..models.sma_sandbox_o_auth_credentials import SMASandboxOAuthCredentials
        from ..models.smao_auth_credentials import SMAOAuthCredentials
        from ..models.solar_edge_credentials import SolarEdgeCredentials
        from ..models.solis_credentials import SolisCredentials

        id = self.id

        name = self.name

        credentials: Dict[str, Any]
        if isinstance(self.credentials, HiddenEnphaseDeveloperAppCredentials):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, HiddenEnphasePartnerAppCredentials):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, HiddenEnphaseVPPCredentials):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, HiddenFranklinWHCredentials):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, HiddenSMACustomGrantCredentials):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, HiddenSMAOAuthCredentials):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, HiddenSMASandboxCustomGrantCredentials):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, HiddenSMASandboxOAuthCredentials):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, HiddenSolarEdgeCredentials):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, HiddenSolisCredentials):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, HiddenTeslaAppCredentials):
            credentials = self.credentials.to_dict()
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
        field_dict.update(
            {
                "id": id,
                "name": name,
                "credentials": credentials,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.enphase_developer_app_credentials import EnphaseDeveloperAppCredentials
        from ..models.enphase_partner_app_credentials import EnphasePartnerAppCredentials
        from ..models.enphase_vpp_credentials import EnphaseVPPCredentials
        from ..models.franklin_wh_credentials import FranklinWHCredentials
        from ..models.hidden_enphase_developer_app_credentials import HiddenEnphaseDeveloperAppCredentials
        from ..models.hidden_enphase_partner_app_credentials import HiddenEnphasePartnerAppCredentials
        from ..models.hidden_enphase_vpp_credentials import HiddenEnphaseVPPCredentials
        from ..models.hidden_franklin_wh_credentials import HiddenFranklinWHCredentials
        from ..models.hidden_sma_custom_grant_credentials import HiddenSMACustomGrantCredentials
        from ..models.hidden_sma_sandbox_custom_grant_credentials import HiddenSMASandboxCustomGrantCredentials
        from ..models.hidden_sma_sandbox_o_auth_credentials import HiddenSMASandboxOAuthCredentials
        from ..models.hidden_smao_auth_credentials import HiddenSMAOAuthCredentials
        from ..models.hidden_solar_edge_credentials import HiddenSolarEdgeCredentials
        from ..models.hidden_solis_credentials import HiddenSolisCredentials
        from ..models.hidden_tesla_app_credentials import HiddenTeslaAppCredentials
        from ..models.sma_custom_grant_credentials import SMACustomGrantCredentials
        from ..models.sma_sandbox_custom_grant_credentials import SMASandboxCustomGrantCredentials
        from ..models.sma_sandbox_o_auth_credentials import SMASandboxOAuthCredentials
        from ..models.smao_auth_credentials import SMAOAuthCredentials
        from ..models.solar_edge_credentials import SolarEdgeCredentials
        from ..models.solis_credentials import SolisCredentials
        from ..models.tesla_app_credentials import TeslaAppCredentials

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        def _parse_credentials(
            data: object,
        ) -> Union[
            "EnphaseDeveloperAppCredentials",
            "EnphasePartnerAppCredentials",
            "EnphaseVPPCredentials",
            "FranklinWHCredentials",
            "HiddenEnphaseDeveloperAppCredentials",
            "HiddenEnphasePartnerAppCredentials",
            "HiddenEnphaseVPPCredentials",
            "HiddenFranklinWHCredentials",
            "HiddenSMACustomGrantCredentials",
            "HiddenSMAOAuthCredentials",
            "HiddenSMASandboxCustomGrantCredentials",
            "HiddenSMASandboxOAuthCredentials",
            "HiddenSolarEdgeCredentials",
            "HiddenSolisCredentials",
            "HiddenTeslaAppCredentials",
            "SMACustomGrantCredentials",
            "SMAOAuthCredentials",
            "SMASandboxCustomGrantCredentials",
            "SMASandboxOAuthCredentials",
            "SolarEdgeCredentials",
            "SolisCredentials",
            "TeslaAppCredentials",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_hidden_vendor_credentials_credentials_type_0 = (
                    HiddenEnphaseDeveloperAppCredentials.from_dict(data)
                )

                return componentsschemas_hidden_vendor_credentials_credentials_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_hidden_vendor_credentials_credentials_type_1 = (
                    HiddenEnphasePartnerAppCredentials.from_dict(data)
                )

                return componentsschemas_hidden_vendor_credentials_credentials_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_hidden_vendor_credentials_credentials_type_2 = HiddenEnphaseVPPCredentials.from_dict(
                    data
                )

                return componentsschemas_hidden_vendor_credentials_credentials_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_hidden_vendor_credentials_credentials_type_3 = HiddenFranklinWHCredentials.from_dict(
                    data
                )

                return componentsschemas_hidden_vendor_credentials_credentials_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_hidden_vendor_credentials_credentials_type_4 = (
                    HiddenSMACustomGrantCredentials.from_dict(data)
                )

                return componentsschemas_hidden_vendor_credentials_credentials_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_hidden_vendor_credentials_credentials_type_5 = HiddenSMAOAuthCredentials.from_dict(
                    data
                )

                return componentsschemas_hidden_vendor_credentials_credentials_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_hidden_vendor_credentials_credentials_type_6 = (
                    HiddenSMASandboxCustomGrantCredentials.from_dict(data)
                )

                return componentsschemas_hidden_vendor_credentials_credentials_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_hidden_vendor_credentials_credentials_type_7 = (
                    HiddenSMASandboxOAuthCredentials.from_dict(data)
                )

                return componentsschemas_hidden_vendor_credentials_credentials_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_hidden_vendor_credentials_credentials_type_8 = HiddenSolarEdgeCredentials.from_dict(
                    data
                )

                return componentsschemas_hidden_vendor_credentials_credentials_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_hidden_vendor_credentials_credentials_type_9 = HiddenSolisCredentials.from_dict(data)

                return componentsschemas_hidden_vendor_credentials_credentials_type_9
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_hidden_vendor_credentials_credentials_type_10 = HiddenTeslaAppCredentials.from_dict(
                    data
                )

                return componentsschemas_hidden_vendor_credentials_credentials_type_10
            except:  # noqa: E722
                pass
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

        credentials = _parse_credentials(d.pop("credentials"))

        update_vendor_credentials_response = cls(
            id=id,
            name=name,
            credentials=credentials,
        )

        return update_vendor_credentials_response
