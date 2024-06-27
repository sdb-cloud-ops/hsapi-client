from typing import *

from pydantic import BaseModel, Field


class v1User(BaseModel):
    """
    None model

    """

    id: Optional[int] = Field(alias="id", default=None)
    name: Optional[str] = Field(alias="name", default=None)
    createdAt: Optional[str] = Field(alias="createdAt", default=None)
