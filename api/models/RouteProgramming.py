from django.db import models
from .Route import Route
from .BusTimetable import BusTimetable


class RouteProgrammingManager(models.Manager):
    """
    RouteProgrammingManager handles the creation of RouteProgramming instances.
    """

    def create_route_programming(self, route, busTimetable):
        """
        Creates an RouteProgramming instance with the given parameters and saves it to the database.
        Args:
            route (Route): The route to which the bus stop belongs.
            busTimetable (BusTimetable): The busTimetable that belongs to the route.
        Returns:
            The newly created RouteProgramming instance.
        """
        if not route and not busTimetable:
            raise ValueError('You must fill in all fields')
        route_programming = self.model(route=route,
                                       busTimetable=busTimetable)
        route_programming.save(using=self._db)
        return route_programming


class RouteProgramming(models.Model):
    """
    RouteProgramming represents the relationship between a Route and a Schedule.
    """
    id = models.AutoField(primary_key=True, db_column='route_programming_id')
    route = models.ForeignKey(Route, on_delete=models.CASCADE, db_column='route_id')
    busTimetable = models.ForeignKey(BusTimetable, on_delete=models.CASCADE, db_column='bus_timetable_id')

    objects = RouteProgrammingManager()

    class Meta:
        managed = False
        db_table = 'route_programming'
        unique_together = (('route', 'busTimetable'),)

    def __str__(self):
        return f'{self.route.name} ({self.busTimetable.hour})'
