from .model import HSAPICall
from headscale_api_client.schemas import (v1ListNodesResponse,
                                          v1GetNodeResponse,
                                          v1DeleteNodeResponse,
                                          v1ExpireNodeResponse, v1MoveNodeRequest,
                                          v1RenameNodeResponse,
                                          v1MoveNodeRequest,
                                          v1MoveNodeResponse,
                                          v1GetNodeRoutesResponse,
                                          v1SetTagsResponse,
                                          HeadscaleServiceSetTagsBody)


class Node(HSAPICall):

    objectPath = "node"

    def list(self) -> v1ListNodesResponse:
        response = self.call('get')
        return v1ListNodesResponse(**response.json())

    def get(self, nodeId: str) -> v1GetNodeResponse:
        response = self.call('get', call_path=nodeId)
        return v1GetNodeResponse(**response.json())

    def delete(self, nodeId: str) -> v1DeleteNodeResponse:
        response = self.call('delete', call_path=nodeId)
        return v1DeleteNodeResponse(**response.json())

    def expire(self, nodeId: str) -> v1ExpireNodeResponse:
        response = self.call('post', f'{nodeId}/expire')
        return v1ExpireNodeResponse()(**response.json())

    def rename(self, nodeId: str, newName: str) -> v1RenameNodeResponse:
        response = self.call('post', f'{nodeId}/rename/{newName}')
        return v1RenameNodeResponse(**response.json())

    def move(self, nodeId: str, data: v1MoveNodeRequest) -> v1MoveNodeResponse:
        response = self.call('post', f'{nodeId}/user', data)
        return v1MoveNodeResponse()(**response.json())

    def routes(self, nodeId: str) -> v1GetNodeRoutesResponse:
        response = self.call('get', f'{nodeId}/routes')
        return v1GetNodeRoutesResponse(**response.json())

    def setTags(self, nodeId: str, data: HeadscaleServiceSetTagsBody) -> v1SetTagsResponse:
        response = self.call('post', f'{nodeId}/tags', data)
        return v1SetTagsResponse(**response.json())
