from .model import HSAPICall
from headscale_api_client.schemas import (v1GetRoutesResponse,
                                          v1DeleteRouteResponse,
                                          v1EnableRouteResponse,
                                          v1DisableRouteResponse,
                                          )


class Route(HSAPICall):

    objectPath = "routes"

    def list(self) -> v1GetRoutesResponse:
        response = self.call('get')
        return v1GetRoutesResponse(**response.json())

    def delete(self, routeId: str) -> v1DeleteRouteResponse:
        response = self.call('delete', call_path=routeId)
        return v1DeleteRouteResponse(**response.json())

    def enable(self, routeId: str) -> v1EnableRouteResponse:
        response = self.call('post', f'{routeId}/enable')
        return v1EnableRouteResponse(**response.json())

    def disable(self, routeId: str) -> v1DisableRouteResponse:
        response = self.call('post', f'{routeId}/disable')
        return v1DisableRouteResponse(**response.json())
