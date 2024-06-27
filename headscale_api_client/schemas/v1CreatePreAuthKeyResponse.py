from typing import *

from pydantic import BaseModel, Field

from .v1PreAuthKey import v1PreAuthKey


class v1CreatePreAuthKeyResponse(BaseModel):
    """
    None model

    """

    preAuthKey: Optional[v1PreAuthKey] = Field(alias="preAuthKey", default=None)
