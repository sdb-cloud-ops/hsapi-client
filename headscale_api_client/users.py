from .model import HSAPICall
from headscale_api_client.schemas import (v1CreateUserRequest,
                                          v1CreateUserResponse,
                                          v1DeleteUserResponse,
                                          v1ListUsersResponse,
                                          v1GetUserResponse,
                                          v1RenameUserResponse,
                                          )


class User(HSAPICall):

    objectPath = "user"

    def list(self) -> v1ListUsersResponse:
        response = self.call('get')
        return v1ListUsersResponse(**response.json())

    def get(self, name: str) -> v1GetUserResponse:
        response = self.call('get', call_path=name)
        return v1GetUserResponse(**response.json())

    def create(self, data: v1CreateUserRequest) -> v1CreateUserResponse:
        response = self.call('post', data=data)
        return v1CreateUserResponse(**response.json())

    def delete(self, name: str) -> v1DeleteUserResponse:
        response = self.call('delete',  name)
        return v1DeleteUserResponse(**response.json())

    def rename(self, oldName: str, newName: str) -> v1RenameUserResponse:
        response = self.call('post',  call_path=f"{oldName}/rename/{newName}")
        return v1RenameUserResponse(**response.json())
