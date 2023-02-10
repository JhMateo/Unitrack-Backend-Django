from django.db import models
from .Route import Route
from .BusStop import BusStop


class RouteBusStopManager(models.Manager):
    """
    RouteBusStopManager handles the creation of RouteBusStop instances.
    """
    def create_route_bus_stop(self, route, busStop):
        """
        Creates an RouteBusStop instance with the given parameters and saves it to the database.
        Args:
            route (Route): The route to which the bus stop belongs.
            busStop (BusStop): The bus stop that belongs to the route.
        Returns:
            The newly created RouteBusStop instance.
        """
        if not route and not busStop:
            raise ValueError('You must fill in all fields')
        route_bus_stop = self.model(route=route,
                                   busStop=busStop)
        route_bus_stop.save(using=self._db)
        return route_bus_stop


class RouteBusStop(models.Model):
    """
    RouteBusStop represents the relationship between a Route and a BusStop.
    """
    id = models.AutoField(primary_key=True, db_column='route_bus_stop_id')
    route = models.ForeignKey(Route, on_delete=models.CASCADE, db_column='route_id')
    busStop = models.ForeignKey(BusStop, on_delete=models.CASCADE, db_column='bus_stop_id')

    objects = RouteBusStopManager()

    class Meta:
        managed = False
        db_table = 'route_bus_stop'
        unique_together = (('route', 'busStop'),)

    def __str__(self):
        return f'{self.route.name} ({self.busStop.place})'
