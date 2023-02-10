from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from api.models import RouteProgramming
from api.serializers import RouteProgrammingSerializer


class RouteProgrammingList(APIView):
    """
    List all route_programmings with soft delete filter.
    """
    permission_classes = (AllowAny,)

    @staticmethod
    @action(methods=['get'], detail=False)
    def get(request):
        """
        Get all route_programmings with soft delete filter.
        Args:
            request: Request from client.

        Returns:
            (Response): Response with all route_programmings.
        """
        route_programmings = RouteProgramming.objects.all()
        route_programmings_serialized = []
        for route_programming in route_programmings:
            route_programmings_serialized.append(RouteProgrammingSerializer.serialize_route_programming(route_programming=route_programming))
        return Response(route_programmings_serialized)


class RouteProgrammingRoute(APIView):
    """
    Retrieve a route_programming by route id.
    """
    permission_classes = (AllowAny,)

    @staticmethod
    @action(methods=['get'], detail=True)
    def get(request, id):
        """
        Get route_programmings by route id.
        Args:
            request: Request from client.
            id (str): Id of the route.

        Returns:
            (Response): Response with the list of route_programmings that belong to the route.
        """
        messages = []
        if not RouteProgramming.objects.filter(route=id).exists():
            messages.append('Esta ruta no existe')
            return Response({"Errors": messages}, status=status.HTTP_404_NOT_FOUND)

        route_programmings = RouteProgramming.objects.filter(route=id)
        route_programmings_serialized = []
        for route_programming in route_programmings:
            route_programmings_serialized.append(RouteProgrammingSerializer.serialize_route_programming(route_programming=route_programming))
        return Response(route_programmings_serialized)
