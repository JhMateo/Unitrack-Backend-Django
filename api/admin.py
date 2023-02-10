from django.contrib import admin
from .models import BusStop, Route, RouteBusStop, BusTimetable, RouteProgramming, User

# Register your models here.
admin.site.register(BusStop)
admin.site.register(Route)
admin.site.register(RouteBusStop)
admin.site.register(BusTimetable)
admin.site.register(RouteProgramming)
admin.site.register(User)