from typing import *

from pydantic import BaseModel, Field

from .v1Node import v1Node


class v1ListNodesResponse(BaseModel):
    """
    None model

    """

    nodes: Optional[List[Optional[v1Node]]] = Field(alias="nodes", default=None)
