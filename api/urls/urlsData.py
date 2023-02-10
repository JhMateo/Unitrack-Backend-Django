from django.urls import path, include
from api.views import RouteList, RouteProgrammingList, RouteProgrammingRoute, BusStopList, BusStopRoute

"""
This file configures all the routes that a user has access to.
"""

urlpatterns = [
    path('routes/', RouteList.as_view(), name='route_list'),

    path('route-programming/', include([
        path('', RouteProgrammingList.as_view(), name='route_programming_list'),
        path('<str:id>', RouteProgrammingRoute.as_view(), name='route_programming')
    ])),

    path('bus-stops/', include([
        path('', BusStopList.as_view(), name='bus_stop_list'),
        path('route/<str:id>', BusStopRoute.as_view(), name='bus_stop_route')
    ])),
]
