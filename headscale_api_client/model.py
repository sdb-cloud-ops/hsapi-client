from typing import Union, Optional, Dict, Any
from .config import APISettings, HTTPException
import requests


def formatTags(tagList: Union[list, None] = []) -> list:
    """
    Get a list of tags and prepend `tag:` to all the ones that
    do not start with `tag:`
    """

    formattedTags = []
    if tagList:
        for tag in tagList:
            formatted = f"tag:{tag}" if not tag.startswith('tag:') else tag
            formattedTags.append(formatted)
    return formattedTags


class HSAPICall:
    """
    Generic API call.
    It has a call() method that wants:
    - a method (GET, POST, DELETE);
    - a subpath, that is appended to <server>/api/v1/{self.objectPath}
    - optional `data` payload, the body of the request
    """

    objectPath: str = ""

    def __init__(self, api_settings_override: Optional[APISettings] = None) -> None:
        if api_settings_override:
            self.api_settings = api_settings_override
        else:
            self.api_settings = APISettings()
        self.base_path = f"{
            self.api_settings.server}{self.api_settings.api_path}/{self.objectPath}"

    def call(self, method, call_path: str = "", data=None, query: dict = {}):
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.api_settings.api_token}",
        }

        json_ = data.dict() if data else dict()

        query_params: Dict[str, Any] = {}
        query_params = {key: value for (
            key, value) in query.items() if value is not None}

        path = '/'.join([self.base_path, str(call_path)]
                        ) if call_path else self.base_path

        response = requests.request(
            method,
            path,
            headers=headers,
            params=query_params,
            verify=self.api_settings.ssl_verify,
            json=json_
        )
        if response.status_code != 200:
            raise HTTPException(response.status_code, f" failed with status code: {
                                response.text}")

        return response
