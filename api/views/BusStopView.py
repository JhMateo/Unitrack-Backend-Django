from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import BusStop, RouteBusStop
from api.serializers import BusStopSerializer
from rest_framework.permissions import AllowAny


class BusStopList(APIView):
    """
    List all bus_stops.
    """
    permission_classes = (AllowAny,)

    @staticmethod
    @action(methods=['get'], detail=False)
    def get(request):
        """
        Get all bus_stops.
        Args:
            request: Request from client.

        Returns:
            (Response): Response with all bus_stops.
        """
        bus_stops = BusStop.objects.all()
        bus_stops_serialized = []
        for bus_stop in bus_stops:
            bus_stops_serialized.append(BusStopSerializer.serialize_bus_stops(bus_stop=bus_stop))
        return Response({'bus_stops': bus_stops_serialized})


class BusStopRoute(APIView):
    """
    Retrieve a bus_stop by route id.
    """
    permission_classes = (AllowAny,)

    @staticmethod
    @action(methods=['get'], detail=True)
    def get(request, id):
        """
        Get bus_stops by route id.
        Args:
            request: Request from client.
            id (str): Id of the route.

        Returns:
            (Response): Response with the list of bus_stops that belong to the route.
        """
        messages = []
        if not RouteBusStop.objects.filter(route=id).exists():
            messages.append('Esta ruta no existe')
            return Response({"Errors": messages}, status=status.HTTP_404_NOT_FOUND)

        bus_stops = RouteBusStop.objects.filter(route=id)
        bus_stops_serialized = []
        for bus_stop in bus_stops:
            bus_stops_serialized.append(BusStopSerializer.serialize_bus_stops(bus_stop=bus_stop.busStop))
        return Response(bus_stops_serialized)
