from .model import HSAPICall
from headscale_api_client.schemas import (v1CreateApiKeyRequest,
                                          v1ListApiKeysResponse,
                                          v1CreateApiKeyResponse,
                                          v1ExpireApiKeyRequest,
                                          v1ExpireApiKeyResponse,
                                          v1DeleteApiKeyResponse)


class APIKey(HSAPICall):

    def list(self) -> v1ListApiKeysResponse:
        response = self.call('get', 'apikey')
        return v1ListApiKeysResponse(**response.json())

    def create(self, data: v1CreateApiKeyRequest) -> v1CreateApiKeyResponse:
        response = self.call('post', 'apikey', data)
        return v1CreateApiKeyResponse(**response.json())

    def expire(self, data: v1ExpireApiKeyRequest) -> v1ExpireApiKeyResponse:
        response = self.call('post', 'apikey/expire', data)
        return v1ExpireApiKeyResponse(**response.json())

    def delete(self, prefix: str) -> v1DeleteApiKeyResponse:
        response = self.call('delete', f'apikey/{prefix}')
        return v1DeleteApiKeyResponse(**response.json())
