from typing import *

from pydantic import BaseModel, Field


class v1DebugCreateNodeRequest(BaseModel):
    """
    None model

    """

    user: Optional[str] = Field(alias="user", default=None)
