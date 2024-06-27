from typing import *

from pydantic import BaseModel, Field


class v1PreAuthKey(BaseModel):
    """
    None model

    """

    user: Optional[str] = Field(alias="user", default=None)

    id: Optional[str] = Field(alias="id", default=None)

    key: Optional[str] = Field(alias="key", default=None)

    reusable: Optional[bool] = Field(alias="reusable", default=None)

    ephemeral: Optional[bool] = Field(alias="ephemeral", default=None)

    used: Optional[bool] = Field(alias="used", default=None)

    expiration: Optional[str] = Field(alias="expiration", default=None)

    createdAt: Optional[str] = Field(alias="createdAt", default=None)

    aclTags: Optional[List[str]] = Field(alias="aclTags", default=None)
