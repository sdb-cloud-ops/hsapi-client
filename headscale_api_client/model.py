from .schemas import *
from .config import APISettings, HTTPException
import requests


class HSAPICall:
    """
    Generic API call.
    It has a call() method that wants:
    - a method (GET, POST, DELETE);
    - a subpath, that is appended to <server>/api/v1
    - optional `data` payload
    """

    objectPath: str = ""

    def __init__(self, api_settings_override: Optional[APISettings] = None) -> None:
        if api_settings_override:
            self.api_settings = api_settings_override
        else:
            self.api_settings = APISettings()
        self.base_path = f"{
            self.api_settings.server}{self.api_settings.api_path}/{self.objectPath}"

    def call(self, method, call_path: str = "", data=None):
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.api_settings.api_token}",
        }

        json_ = data.dict() if data else dict()

        path = '/'.join([self.base_path, str(call_path)]
                        ) if call_path else self.base_path

        response = requests.request(
            method,
            path,
            headers=headers,
            verify=self.api_settings.ssl_verify,
            json=json_
        )
        if response.status_code != 200:
            raise HTTPException(response.status_code, f" failed with status code: {
                                response.text}")

        return response
