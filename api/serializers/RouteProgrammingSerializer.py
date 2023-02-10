from rest_framework import serializers
from ..models import RouteProgramming


class RouteProgrammingSerializer(serializers.ModelSerializer):
    """
    Serializer for RouteProgramming model
    """
    def serialize_route_programming(route_programming):
        """
        Returns serialized representation of a service
        Args:
            route_programming (RouteProgramming): Instance of Service model
        Returns:
            dict: serialized representation of a service
        """

        return {
            'id': route_programming.id,
            'routeId': route_programming.route.id,
            'routeName': route_programming.route.name,
            'busTimetableId': route_programming.busTimetable.id,
            'busTimetable': route_programming.busTimetable.hour.strftime('%H:%M:%S')
        }

    class Meta:
        model = RouteProgramming
        fields = (
            'id',
            'route',
            'busTimetable'
        )
