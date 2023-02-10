from rest_framework import serializers
from ..models import BusStop


class BusStopSerializer(serializers.ModelSerializer):
    """
    Serializer for BusStop model
    """
    def serialize_bus_stops(bus_stop):
        """
        Returns serialized representation of a bus_stop
        Args:
            bus_stop (BusStop): Instance of BusStop model
        Returns:
            dict: serialized representation of a bus_stop
        """
        coordinates = {
            'lat': bus_stop.latitude,
            'lng': bus_stop.length
        }
        return {
            'id': bus_stop.id,
            'place': bus_stop.place,
            'details': bus_stop.details,
            'coordinates': coordinates
        }

    class Meta:
        model = BusStop
        fields = (
            'id',
            'place',
            'details',
            'length',
            'latitude'
        )
