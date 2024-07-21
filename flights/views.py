from rest_framework import viewsets
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


class RouteListViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.select_related('source', 'destination').all()
    serializer_class = RouteSerializer


class AirportListViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class AirplaneListViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.select_related('airplane_type').all()
    serializer_class = AirplaneSerializer


class AirplaneTypeListViewSet(viewsets.ModelViewSet):
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeSerializer


class OrderListViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class TicketListViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.select_related('flight', 'order').all()
    serializer_class = TicketSerializer


class FlightListViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.select_related('route__source', 'route__destination', 'airplane__airplane_type').prefetch_related('crew').all()
    serializer_class = FlightSerializer
