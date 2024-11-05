from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

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


T = TypeVar("T", bound="CreateVendorCredentialsRequest")


@_attrs_define
class CreateVendorCredentialsRequest:
    """
    Attributes:
        credentials (Union['EnphaseDeveloperAppCredentials', 'EnphasePartnerAppCredentials', 'EnphaseVPPCredentials',
            'FranklinWHCredentials', 'SMACustomGrantCredentials', 'SMAOAuthCredentials', 'SMASandboxCustomGrantCredentials',
            'SMASandboxOAuthCredentials', 'SolarEdgeCredentials', 'SolisCredentials', 'TeslaAppCredentials']): Credentials
            for a given vendor.
        name (Union[Unset, str]): The name of the vendor credentials; inferred if not provided.
    """

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
    ]
    name: Union[Unset, str] = UNSET

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

        credentials: Dict[str, Any]
        if isinstance(self.credentials, EnphasePartnerAppCredentials):
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

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "credentials": credentials,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

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
        ]:
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

        name = d.pop("name", UNSET)

        create_vendor_credentials_request = cls(
            credentials=credentials,
            name=name,
        )

        return create_vendor_credentials_request
