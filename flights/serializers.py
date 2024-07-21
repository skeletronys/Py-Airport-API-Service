from rest_framework import serializers

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


class CrewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crew
        fields = "__all__"


class AirportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airport
        fields = "__all__"


class RouteSerializer(serializers.ModelSerializer):
    source = serializers.SlugRelatedField(queryset=Airport.objects.all(), slug_field="name")
    destination = serializers.SlugRelatedField(queryset=Airport.objects.all(), slug_field="name")

    class Meta:
        model = Route
        fields = "__all__"


class AirplaneTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AirplaneType
        fields = "__all__"


class AirplaneSerializer(serializers.ModelSerializer):
    airplane_type = AirplaneTypeSerializer(read_only=True)
    airplane_type_id = serializers.PrimaryKeyRelatedField(
        queryset=AirplaneType.objects.all(),
        source="airplane_type",
        write_only=True
    )

    class Meta:
        model = Airplane
        fields = ("id", "name", "rows", "seats_in_row", "airplane_type_id", "airplane_type")


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        created_at = instance.created_at
        formatted_created_at = created_at.strftime("%H:%M:%S %d-%m-%Y")
        representation["created_at"] = formatted_created_at
        return representation


class FlightSerializer(serializers.ModelSerializer):
    airplane = serializers.SlugRelatedField(
        queryset=Airplane.objects.all(),
        slug_field="name"
    )
    crew = serializers.PrimaryKeyRelatedField(queryset=Crew.objects.all(), many=True)
    route = serializers.PrimaryKeyRelatedField(queryset=Route.objects.all())

    class Meta:
        model = Flight
        fields = ("id", "crew", "route", "airplane", "departure_time", "arrival_time")

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        route_data = instance.route
        if route_data:
            representation["route"] = f"{route_data.source.name} - {route_data.destination.name}"

        crew_data = CrewSerializer(instance.crew.all(), many=True).data
        representation["crew"] = crew_data

        return representation


class TicketSerializer(serializers.ModelSerializer):
    flight = serializers.PrimaryKeyRelatedField(queryset=Flight.objects.all(), write_only=True)
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(), write_only=True)

    class Meta:
        model = Ticket
        fields = ("id", "flight", "order", "row", "seat")

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        flight_data = instance.flight
        if flight_data:
            flight_representation = FlightSerializer(flight_data).data
            flight_representation['departure_time'] = flight_data.departure_time.strftime("%H:%M:%S %d-%m-%Y")
            flight_representation['arrival_time'] = flight_data.arrival_time.strftime("%H:%M:%S %d-%m-%Y")
            representation['flight'] = flight_representation

        order_data = instance.order
        if order_data:
            order_representation = OrderSerializer(order_data).data
            order_representation['created_at'] = order_data.created_at.strftime("%H:%M:%S %d-%m-%Y")
            order_representation['user'] = order_data.user.username
            representation['order'] = order_representation

        return representation
