from typing import *

from pydantic import BaseModel, Field

from .protobufAny import protobufAny


class rpcStatus(BaseModel):
    """
    None model

    """

    code: Optional[int] = Field(alias="code", default=None)

    message: Optional[str] = Field(alias="message", default=None)

    details: Optional[List[Optional[protobufAny]]] = Field(alias="details", default=None)
