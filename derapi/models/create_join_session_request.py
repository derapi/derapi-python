from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.enphase_join_config import EnphaseJoinConfig
    from ..models.enphase_vpp_join_config import EnphaseVPPJoinConfig
    from ..models.sma_join_config import SMAJoinConfig
    from ..models.sma_sandbox_join_config import SMASandboxJoinConfig
    from ..models.solaredge_join_config import SolaredgeJoinConfig
    from ..models.solis_join_config import SolisJoinConfig
    from ..models.tesla_join_config import TeslaJoinConfig


T = TypeVar("T", bound="CreateJoinSessionRequest")


@_attrs_define
class CreateJoinSessionRequest:
    """
    Attributes:
        store_credentials (bool): Whether Derapi should store the credentials received from Join. If enabled, requires
            VCM.
        vendors (List[Union['EnphaseJoinConfig', 'EnphaseVPPJoinConfig', 'SMAJoinConfig', 'SMASandboxJoinConfig',
            'SolaredgeJoinConfig', 'SolisJoinConfig', 'TeslaJoinConfig']]): Add an object for each vendor that should appear
            in the UI
    """

    store_credentials: bool
    vendors: List[
        Union[
            "EnphaseJoinConfig",
            "EnphaseVPPJoinConfig",
            "SMAJoinConfig",
            "SMASandboxJoinConfig",
            "SolaredgeJoinConfig",
            "SolisJoinConfig",
            "TeslaJoinConfig",
        ]
    ]

    def to_dict(self) -> Dict[str, Any]:
        from ..models.enphase_join_config import EnphaseJoinConfig
        from ..models.enphase_vpp_join_config import EnphaseVPPJoinConfig
        from ..models.sma_join_config import SMAJoinConfig
        from ..models.sma_sandbox_join_config import SMASandboxJoinConfig
        from ..models.solaredge_join_config import SolaredgeJoinConfig
        from ..models.solis_join_config import SolisJoinConfig

        store_credentials = self.store_credentials

        vendors = []
        for vendors_item_data in self.vendors:
            vendors_item: Dict[str, Any]
            if isinstance(vendors_item_data, EnphaseJoinConfig):
                vendors_item = vendors_item_data.to_dict()
            elif isinstance(vendors_item_data, EnphaseVPPJoinConfig):
                vendors_item = vendors_item_data.to_dict()
            elif isinstance(vendors_item_data, SMAJoinConfig):
                vendors_item = vendors_item_data.to_dict()
            elif isinstance(vendors_item_data, SMASandboxJoinConfig):
                vendors_item = vendors_item_data.to_dict()
            elif isinstance(vendors_item_data, SolaredgeJoinConfig):
                vendors_item = vendors_item_data.to_dict()
            elif isinstance(vendors_item_data, SolisJoinConfig):
                vendors_item = vendors_item_data.to_dict()
            else:
                vendors_item = vendors_item_data.to_dict()

            vendors.append(vendors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "storeCredentials": store_credentials,
                "vendors": vendors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.enphase_join_config import EnphaseJoinConfig
        from ..models.enphase_vpp_join_config import EnphaseVPPJoinConfig
        from ..models.sma_join_config import SMAJoinConfig
        from ..models.sma_sandbox_join_config import SMASandboxJoinConfig
        from ..models.solaredge_join_config import SolaredgeJoinConfig
        from ..models.solis_join_config import SolisJoinConfig
        from ..models.tesla_join_config import TeslaJoinConfig

        d = src_dict.copy()
        store_credentials = d.pop("storeCredentials")

        vendors = []
        _vendors = d.pop("vendors")
        for vendors_item_data in _vendors:

            def _parse_vendors_item(
                data: object,
            ) -> Union[
                "EnphaseJoinConfig",
                "EnphaseVPPJoinConfig",
                "SMAJoinConfig",
                "SMASandboxJoinConfig",
                "SolaredgeJoinConfig",
                "SolisJoinConfig",
                "TeslaJoinConfig",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    vendors_item_type_0 = EnphaseJoinConfig.from_dict(data)

                    return vendors_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    vendors_item_type_1 = EnphaseVPPJoinConfig.from_dict(data)

                    return vendors_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    vendors_item_type_2 = SMAJoinConfig.from_dict(data)

                    return vendors_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    vendors_item_type_3 = SMASandboxJoinConfig.from_dict(data)

                    return vendors_item_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    vendors_item_type_4 = SolaredgeJoinConfig.from_dict(data)

                    return vendors_item_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    vendors_item_type_5 = SolisJoinConfig.from_dict(data)

                    return vendors_item_type_5
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                vendors_item_type_6 = TeslaJoinConfig.from_dict(data)

                return vendors_item_type_6

            vendors_item = _parse_vendors_item(vendors_item_data)

            vendors.append(vendors_item)

        create_join_session_request = cls(
            store_credentials=store_credentials,
            vendors=vendors,
        )

        return create_join_session_request
