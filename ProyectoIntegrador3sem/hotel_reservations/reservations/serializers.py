# reservations/serializers.py

from rest_framework import serializers
from .models import Room, Client, Reservation, Rate, Availability

# Serializadores
class RoomSerializer(serializers.ModelSerializer):
    """
    Serializador para la clase Room.
    """
    class Meta:
        model = Room
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    """
    Serializador para la clase Client.
    """
    class Meta:
        model = Client
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    """
    Serializador para la clase Reservation.
    """
    class Meta:
        model = Reservation
        fields = '__all__'

class RateSerializer(serializers.ModelSerializer):
    """
    Serializador para la clase Rate.
    """
    class Meta:
        model = Rate
        fields = '__all__'

class AvailabilitySerializer(serializers.ModelSerializer):
    """
    Serializador para la clase Availability.
    """
    class Meta:
        model = Availability
        fields = '__all__'
