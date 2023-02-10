from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Route
from api.serializers import RouteSerializer
from rest_framework.permissions import AllowAny


class RouteList(APIView):
    """
    List all routes.
    """
    permission_classes = (AllowAny,)

    @staticmethod
    @action(methods=['get'], detail=False)
    def get(request):
        """
        Get all routes.
        Args:
            request: Request from client.

        Returns:
            (Response): Response with all routes.
        """
        routes = Route.objects.filter(direction=0)
        routes_serialized = []
        for route in routes:
            routes_serialized.append(RouteSerializer.serialize_routes(route=route))
        return Response({'routes': routes_serialized})
