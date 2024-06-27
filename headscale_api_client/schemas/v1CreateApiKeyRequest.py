from typing import *

from pydantic import BaseModel, Field


class v1CreateApiKeyRequest(BaseModel):
    """
    None model

    """

    expiration: Optional[str] = Field(alias="expiration", default=None)
