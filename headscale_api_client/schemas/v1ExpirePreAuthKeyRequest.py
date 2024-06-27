from typing import *

from pydantic import BaseModel, Field


class v1ExpirePreAuthKeyRequest(BaseModel):
    """
    None model

    """

    user: Optional[str] = Field(alias="user", default=None)

    key: Optional[str] = Field(alias="key", default=None)
