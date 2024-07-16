from rest_framework import mixins, viewsets
from flights.models import (
    Crew,
    Route,
    Airport,
    Airplane,
    AirplaneType,
    Order,
    Ticket,
    Flight
)
from flights.serializers import (
    CrewSerializer,
    RouteSerializer,
    AirportSerializer,
    AirplaneSerializer,
    AirplaneTypeSerializer,
    OrderSerializer,
    TicketSerializer,
    FlightSerializer
)


class CrewListViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
