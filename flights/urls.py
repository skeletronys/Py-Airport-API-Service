from django.urls import path, include
from rest_framework import routers

from flights.views import CrewListViewSet

router = routers.DefaultRouter()
router.register("crew", CrewListViewSet)

app_name = "flights"

urlpatterns = [path("", include(router.urls))]
