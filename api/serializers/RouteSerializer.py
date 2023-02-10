from rest_framework import serializers
from ..models import Route


class RouteSerializer(serializers.ModelSerializer):
    """
    Serializer for Route model
    """
    def serialize_routes(route):
        """
        Returns serialized representation of a route
        Args:
            route (Route): Instance of Route model
        Returns:
            dict: serialized representation of a route
        """

        return {
            'id': route.id,
            'name': route.name,
            'direction': route.direction
        }

    class Meta:
        model = Route
        fields = (
            'id',
            'name',
            'direction'
        )
