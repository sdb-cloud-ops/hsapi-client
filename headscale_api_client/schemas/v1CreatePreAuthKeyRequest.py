from typing import *

from pydantic import BaseModel, Field


class v1CreatePreAuthKeyRequest(BaseModel):
    """
    None model

    """

    user: Optional[str] = Field(alias="user", default=None)

    reusable: Optional[bool] = Field(alias="reusable", default=None)

    ephemeral: Optional[bool] = Field(alias="ephemeral", default=None)

    expiration: Optional[str] = Field(alias="expiration", default=None)

    aclTags: Optional[List[str]] = Field(alias="aclTags", default=None)
