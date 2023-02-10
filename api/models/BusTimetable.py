from django.db import models
from django.utils import timezone


class BusTimetableManager(models.Manager):
    """
    Manager class for the BusTimetable model, provides an additional method for creating bus_timetables
    """
    def create_bus_timetable(self, hour):
        """
        Creates an bus_timetable object with the provided data.

        Args:
            hour (time): The hour the route passes.

        Returns:
            BusTimetable: The created bus_timetable object.

        Raises:
            ValueError: If hour is not provided.
        """
        if not hour:
            raise ValueError('You must provide the hour')
        bus_timetable = self.model(hour=hour)
        bus_timetable.save(using=self._db)
        return bus_timetable


class BusTimetable(models.Model):
    """
    Model representing an BusTimetable object.
    """
    id = models.AutoField(primary_key=True, db_column='bus_timetable_id')
    hour = models.DateTimeField(default=timezone.now)

    objects = BusTimetableManager()

    class Meta:
        managed = False
        db_table = 'bus_timetable'

    def __str__(self):
        return self.hour
