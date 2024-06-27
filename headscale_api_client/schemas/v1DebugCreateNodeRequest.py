from typing import *

from pydantic import BaseModel, Field


class v1DebugCreateNodeRequest(BaseModel):
    """
    None model

    """

    user: Optional[str] = Field(alias="user", default=None)

    key: Optional[str] = Field(alias="key", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    routes: Optional[List[str]] = Field(alias="routes", default=None)
