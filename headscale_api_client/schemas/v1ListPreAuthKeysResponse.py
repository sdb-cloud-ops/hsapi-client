from typing import *

from pydantic import BaseModel, Field

from .v1PreAuthKey import v1PreAuthKey


class v1ListPreAuthKeysResponse(BaseModel):
    """
    None model

    """

    preAuthKeys: Optional[List[Optional[v1PreAuthKey]]] = Field(alias="preAuthKeys", default=None)
