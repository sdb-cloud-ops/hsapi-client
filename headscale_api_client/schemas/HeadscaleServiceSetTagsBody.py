from typing import *

from pydantic import BaseModel, Field


class HeadscaleServiceSetTagsBody(BaseModel):
    """
    None model

    """

    tags: Optional[List[str]] = Field(alias="tags", default=None)
