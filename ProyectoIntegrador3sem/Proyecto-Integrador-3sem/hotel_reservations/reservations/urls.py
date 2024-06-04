# reservations/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, ClientViewSet, ReservationViewSet, RateViewSet, AvailabilityViewSet

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'rates', RateViewSet)
router.register(r'availabilities', AvailabilityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]