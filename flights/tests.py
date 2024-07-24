from datetime import datetime

from django.utils.timezone import make_aware
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from flights.models import (
    Crew,
    Route,
    Airport,
    Airplane,
    AirplaneType,
    Order,
    Ticket,
    Flight,
)
from flights.serializers import (
    CrewSerializer,
    RouteSerializer,
    AirportSerializer,
    AirplaneSerializer,
    AirplaneTypeSerializer,
    OrderSerializer,
    TicketSerializer,
    FlightSerializer,
)


class CrewTest(APITestCase):

    def setUp(self):
        self.crew = Crew.objects.create(first_name="John", last_name="Doe")

    def test_crew_viewset(self):
        url = reverse("flights:crew-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_crew_serialization(self):
        serializer = CrewSerializer(self.crew)
        self.assertEqual(serializer.data["first_name"], self.crew.first_name)
        self.assertEqual(serializer.data["last_name"], self.crew.last_name)


class AirportTest(APITestCase):

    def setUp(self):
        self.airport = Airport.objects.create(
            name="Test Airport", closest_big_city="Test City"
        )

    def test_airport_viewset(self):
        url = reverse("flights:airport-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_airport_serialization(self):
        serializer = AirportSerializer(self.airport)
        self.assertEqual(serializer.data["name"], self.airport.name)
        self.assertEqual(
            serializer.data["closest_big_city"], self.airport.closest_big_city
        )


class OrderTest(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpass"
        )
        self.order = Order.objects.create(user=self.user)

    def test_order_viewset(self):
        url = reverse("flights:order-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_serialization(self):
        serializer = OrderSerializer(self.order)
        self.assertEqual(serializer.data["user"], self.order.user.id)


class AirplaneTypeTest(APITestCase):

    def setUp(self):
        self.airplane_type = AirplaneType.objects.create(name="Type A")

    def test_airplane_type_viewset(self):
        url = reverse("flights:airplanetype-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_airplane_type_serialization(self):
        serializer = AirplaneTypeSerializer(self.airplane_type)
        self.assertEqual(serializer.data["name"], self.airplane_type.name)


class RouteTest(APITestCase):

    def setUp(self):
        self.source = Airport.objects.create(
            name="Airport 1", closest_big_city="City 1"
        )
        self.destination = Airport.objects.create(
            name="Airport 2", closest_big_city="City 2"
        )
        self.route = Route.objects.create(
            source=self.source, destination=self.destination, distance=1000
        )

    def test_route_viewset(self):
        url = reverse("flights:route-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_route_serialization(self):
        serializer = RouteSerializer(self.route)
        self.assertEqual(
            serializer.data["source"], self.route.source.name
        )  # Очікуємо назву аеропорту
        self.assertEqual(
            serializer.data["destination"], self.route.destination.name
        )  # Очікуємо назву аеропорту
        self.assertEqual(serializer.data["distance"], self.route.distance)


class AirplaneTest(APITestCase):

    def setUp(self):
        self.airplane_type = AirplaneType.objects.create(name="Type A")
        self.airplane = Airplane.objects.create(
            name="Boeing 737", rows=20, seats_in_row=6, airplane_type=self.airplane_type
        )

    def test_airplane_viewset(self):
        url = reverse("flights:airplane-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_airplane_serialization(self):
        serializer = AirplaneSerializer(self.airplane)
        self.assertEqual(serializer.data["name"], self.airplane.name)
        self.assertEqual(serializer.data["rows"], self.airplane.rows)
        self.assertEqual(serializer.data["seats_in_row"], self.airplane.seats_in_row)
        self.assertEqual(
            serializer.data["airplane_type"]["id"], self.airplane.airplane_type.id
        )
        self.assertEqual(
            serializer.data["airplane_type"]["name"], self.airplane.airplane_type.name
        )


class FlightTest(APITestCase):

    def setUp(self):
        self.airplane_type = AirplaneType.objects.create(name="Type A")
        self.airplane = Airplane.objects.create(
            name="Boeing 737", rows=20, seats_in_row=6, airplane_type=self.airplane_type
        )
        self.source = Airport.objects.create(
            name="Airport 1", closest_big_city="City 1"
        )
        self.destination = Airport.objects.create(
            name="Airport 2", closest_big_city="City 2"
        )
        self.route = Route.objects.create(
            source=self.source, destination=self.destination, distance=1000
        )
        self.flight = Flight.objects.create(
            route=self.route,
            airplane=self.airplane,
            departure_time=make_aware(
                datetime.strptime("2023-07-20T08:00:00Z", "%Y-%m-%dT%H:%M:%SZ")
            ),
            arrival_time=make_aware(
                datetime.strptime("2023-07-20T10:00:00Z", "%Y-%m-%dT%H:%M:%SZ")
            ),
        )

    def test_flight_viewset(self):
        url = reverse("flights:flight-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_flight_serialization(self):
        serializer = FlightSerializer(self.flight)
        self.assertEqual(
            serializer.data["route"],
            f"{self.route.source.name} - {self.route.destination.name}",
        )
        self.assertEqual(serializer.data["airplane"], self.airplane.name)


class TicketTest(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpass"
        )
        self.order = Order.objects.create(user=self.user)
        self.airplane_type = AirplaneType.objects.create(name="Type A")
        self.airplane = Airplane.objects.create(
            name="Boeing 737", rows=20, seats_in_row=6, airplane_type=self.airplane_type
        )
        self.source = Airport.objects.create(
            name="Airport 1", closest_big_city="City 1"
        )
        self.destination = Airport.objects.create(
            name="Airport 2", closest_big_city="City 2"
        )
        self.route = Route.objects.create(
            source=self.source, destination=self.destination, distance=1000
        )
        self.flight = Flight.objects.create(
            route=self.route,
            airplane=self.airplane,
            departure_time=make_aware(
                datetime.strptime("2023-07-20T08:00:00Z", "%Y-%m-%dT%H:%M:%SZ")
            ),
            arrival_time=make_aware(
                datetime.strptime("2023-07-20T10:00:00Z", "%Y-%m-%dT%H:%M:%SZ")
            ),
        )
        self.ticket = Ticket.objects.create(
            row=1, seat=1, flight=self.flight, order=self.order
        )

    def test_ticket_viewset(self):
        url = reverse("flights:ticket-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ticket_serialization(self):
        serializer = TicketSerializer(self.ticket)
        self.assertEqual(serializer.data["row"], self.ticket.row)
        self.assertEqual(serializer.data["seat"], self.ticket.seat)
        self.assertEqual(serializer.data["flight"]["id"], self.flight.id)
        self.assertEqual(serializer.data["order"]["id"], self.order.id)
