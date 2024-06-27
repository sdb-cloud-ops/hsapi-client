from typing import *

from pydantic import BaseModel, Field

from .v1Node import v1Node


class v1MoveNodeResponse(BaseModel):
    """
    None model

    """

    node: Optional[v1Node] = Field(alias="node", default=None)
