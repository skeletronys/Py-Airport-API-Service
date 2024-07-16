from django.urls import path, include
from rest_framework import routers

from flights.views import (
    CrewListViewSet,
    RouteListViewSet,
    AirportListViewSet,
    AirplaneListViewSet,
    AirplaneTypeListViewSet,
    OrderListViewSet,
    TicketListViewSet,
    FlightListViewSet,
)

router = routers.DefaultRouter()
router.register("crew", CrewListViewSet)
router.register("route", RouteListViewSet)
router.register("airport", AirportListViewSet)
router.register("airplane", AirplaneListViewSet)
router.register("airplanetype", AirplaneTypeListViewSet)
router.register("order", OrderListViewSet)
router.register("ticket", TicketListViewSet)
router.register("flight", FlightListViewSet)


app_name = "flights"

urlpatterns = [path("", include(router.urls))]
