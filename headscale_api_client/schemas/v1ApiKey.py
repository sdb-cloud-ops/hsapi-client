from typing import *

from pydantic import BaseModel, Field


class v1ApiKey(BaseModel):
    """
    None model

    """

    id: Optional[str] = Field(alias="id", default=None)

    prefix: Optional[str] = Field(alias="prefix", default=None)

    expiration: Optional[str] = Field(alias="expiration", default=None)

    createdAt: Optional[str] = Field(alias="createdAt", default=None)

    lastSeen: Optional[str] = Field(alias="lastSeen", default=None)
