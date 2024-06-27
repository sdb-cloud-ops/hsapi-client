from typing import *

from pydantic import BaseModel, Field

from .v1User import v1User


class v1ListUsersResponse(BaseModel):
    """
    None model

    """

    users: Optional[List[Optional[v1User]]] = Field(alias="users", default=None)
