from typing import *

from pydantic import BaseModel, Field


class protobufAny(BaseModel):
    """
    None model

    """

    type: Optional[str] = Field(alias="@type", default=None)
