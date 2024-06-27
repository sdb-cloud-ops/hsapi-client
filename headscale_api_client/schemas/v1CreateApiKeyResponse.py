from typing import *

from pydantic import BaseModel, Field


class v1CreateApiKeyResponse(BaseModel):
    """
    None model

    """

    apiKey: Optional[str] = Field(alias="apiKey", default=None)
