from typing import *

from pydantic import BaseModel, Field

from .v1PreAuthKey import v1PreAuthKey
from .v1RegisterMethod import v1RegisterMethod
from .v1User import v1User


class v1Node(BaseModel):
    """
    None model

    """

    id: Optional[int] = Field(alias="id", default=None)
    machineKey: Optional[str] = Field(alias="machineKey", default=None)
    nodeKey: Optional[str] = Field(alias="nodeKey", default=None)
    discoKey: Optional[str] = Field(alias="discoKey", default=None)
    ipAddresses: Optional[List[str]] = Field(alias="ipAddresses", default=None)
    name: Optional[str] = Field(alias="name", default=None)
    user: Optional[v1User] = Field(alias="user", default=None)
    lastSeen: Optional[str] = Field(alias="lastSeen", default=None)
    expiry: Optional[str] = Field(alias="expiry", default=None)
    preAuthKey: Optional[v1PreAuthKey] = Field(
        alias="preAuthKey", default=None)

    createdAt: Optional[str] = Field(alias="createdAt", default=None)
    registerMethod: Optional[v1RegisterMethod] = Field(
        alias="registerMethod", default=None)

    forcedTags: Optional[List[str]] = Field(alias="forcedTags", default=None)
    invalidTags: Optional[List[str]] = Field(alias="invalidTags", default=None)
    validTags: Optional[List[str]] = Field(alias="validTags", default=None)
    givenName: Optional[str] = Field(alias="givenName", default=None)
    online: Optional[bool] = Field(alias="online", default=None)
