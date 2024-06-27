from typing import *

from pydantic import BaseModel, Field


class v1BackfillNodeIPsResponse(BaseModel):
    """
    None model

    """

    changes: Optional[List[str]] = Field(alias="changes", default=None)
