from typing import *

from pydantic import BaseModel, Field


class v1ExpireApiKeyRequest(BaseModel):
    """
    None model

    """

    prefix: Optional[str] = Field(alias="prefix", default=None)
