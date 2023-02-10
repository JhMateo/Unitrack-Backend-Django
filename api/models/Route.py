from django.db import models


class RouteManager(models.Manager):
    """
    Manager class for the Route model, provides an additional method for creating routes
    """
    def create_route(self, id, name, direction):
        """
        Creates an route object with the provided data.

        Args:
            id (str): The id of the route.
            name (str): The name of the route.
            direction (int): 0 if going to university, 1 if going to Vilavicencio.

        Returns:
            Route: The created route object.

        Raises:
            ValueError: If name is not provided.
        """
        if not id:
            raise ValueError('You must provide the id')
        route = self.model(id=id,
                            name=name,
                            direction=direction)
        route.save(using=self._db)
        return route


class Route(models.Model):
    """
    Model representing a Route object.
    """
    id = models.CharField(primary_key=True, max_length=15, db_column='route_id')
    name = models.CharField(max_length=30, db_column='route_name')
    direction = models.IntegerField()

    objects = RouteManager()

    class Meta:
        managed = False
        db_table = 'route'

    def __str__(self):
        return self.name
