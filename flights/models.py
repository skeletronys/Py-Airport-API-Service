from django.db import models
from django.contrib.auth.models import User


class Crew(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)


class Airport(models.Model):
    name = models.CharField(max_length=255)
    closest_big_city = models.CharField(max_length=255)


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class AirplaneType(models.Model):
    name = models.CharField(max_length=255)


class Route(models.Model):
    source = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="routes")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="routes")


class Airplane(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()
    airplane_type = models.ForeignKey(AirplaneType, on_delete=models.CASCADE, related_name="airplanes")


class Flight(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="flights")
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name="flights")
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    crew = models.ManyToManyField(Crew)


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="tickets")
    order = models.ForeignKey(Order, on_delete=models, related_name="tickets")
