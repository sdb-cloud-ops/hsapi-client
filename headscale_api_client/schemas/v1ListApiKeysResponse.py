from typing import *

from pydantic import BaseModel, Field

from .v1ApiKey import v1ApiKey


class v1ListApiKeysResponse(BaseModel):
    """
    None model

    """

    apiKeys: Optional[List[Optional[v1ApiKey]]] = Field(alias="apiKeys", default=None)
