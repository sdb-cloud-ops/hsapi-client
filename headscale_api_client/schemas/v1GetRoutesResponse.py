from typing import *

from pydantic import BaseModel, Field

from .v1Route import v1Route


class v1GetRoutesResponse(BaseModel):
    """
    None model

    """

    routes: Optional[List[Optional[v1Route]]] = Field(alias="routes", default=None)
