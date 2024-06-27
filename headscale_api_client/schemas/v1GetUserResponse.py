from typing import *

from pydantic import BaseModel, Field

from .v1User import v1User


class v1GetUserResponse(BaseModel):
    """
    None model

    """

    user: Optional[v1User] = Field(alias="user", default=None)
