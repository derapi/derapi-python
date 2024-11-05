from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateJoinSessionResponse")


@_attrs_define
class CreateJoinSessionResponse:
    """
    Attributes:
        session_id (str): session token to pass to Join JS component function createJoin()
    """

    session_id: str

    def to_dict(self) -> Dict[str, Any]:
        session_id = self.session_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "sessionID": session_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        session_id = d.pop("sessionID")

        create_join_session_response = cls(
            session_id=session_id,
        )

        return create_join_session_response
