import os
from typing import Optional, Union

from pydantic_settings import BaseSettings, SettingsConfigDict


class APISettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='HS_')
    server: str = "http://localhost:8080"
    api_path: str = "/api/v1"
    ssl_verify: Union[bool, str] = True
    api_token: Union[None, str] = None

    def refresh_api_token(self):
        self.api_token = os.environ.get('HS_API_TOKEN')


class HTTPException(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"{status_code} {message}")

    def __str__(self):
        return f"{self.status_code} {self.message}"
