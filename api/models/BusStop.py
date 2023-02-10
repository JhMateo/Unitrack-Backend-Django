from django.db import models


class BusStopManager(models.Manager):
    """
    Manager class for the BusStop model, provides an additional method for creating bus_stops
    """
    def create_bus_stop(self, id, **extra_fields):
        """
        Creates an bus_stop object with the provided data.

        Args:
            id (str): The id of the bus_stop.
            extra_fields: Additional fields for the bus_stop (**kwargs)

        Returns:
            BusStop: The created bus_stop object.

        Raises:
            ValueError: If id is not provided.
        """
        if not id:
            raise ValueError('You must provide the id')
        bus_stop = self.model(id=id,
                            **extra_fields)

        bus_stop.save(using=self._db)
        return bus_stop


class BusStop(models.Model):
    """
    Model representing an BusStop object.
    """
    id = models.CharField(primary_key=True, max_length=15, db_column='bus_stop_id')
    place = models.CharField(max_length=50)
    details = models.CharField(max_length=200)
    length = models.FloatField()
    latitude = models.FloatField()
    
    objects = BusStopManager()

    class Meta:
        managed = False
        db_table = 'bus_stop'

    def __str__(self):
        return self.place
