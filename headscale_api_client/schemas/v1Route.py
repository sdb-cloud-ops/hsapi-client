from typing import *

from pydantic import BaseModel, Field

from .v1Node import v1Node


class v1Route(BaseModel):
    """
    None model

    """

    id: Optional[int] = Field(alias="id", default=None)
    node: Optional[v1Node] = Field(alias="node", default=None)
    prefix: Optional[str] = Field(alias="prefix", default=None)
    advertised: Optional[bool] = Field(alias="advertised", default=None)
    enabled: Optional[bool] = Field(alias="enabled", default=None)
    isPrimary: Optional[bool] = Field(alias="isPrimary", default=None)
    createdAt: Optional[str] = Field(alias="createdAt", default=None)
    updatedAt: Optional[str] = Field(alias="updatedAt", default=None)
    deletedAt: Optional[str] = Field(alias="deletedAt", default=None)
