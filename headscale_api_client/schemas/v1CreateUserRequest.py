from typing import *

from pydantic import BaseModel, Field


class v1CreateUserRequest(BaseModel):
    """
    None model

    """

    name: Optional[str] = Field(alias="name", default=None)
