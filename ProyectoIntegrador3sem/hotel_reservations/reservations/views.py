from rest_framework import viewsets
from .models import Room, Client, Reservation, Rate, Availability
from .serializers import RoomSerializer, ClientSerializer, ReservationSerializer, RateSerializer, AvailabilitySerializer

class RoomViewSet(viewsets.ModelViewSet):
    """
    Vista para las operaciones CRUD de la clase Room.
    """
    queryset = Room.objects.all()  # Obtiene todas las habitaciones de la base de datos
    serializer_class = RoomSerializer  # Usa el serializador RoomSerializer para convertir los objetos Room en datos JSON

class ClientViewSet(viewsets.ModelViewSet):
    """
    Vista para las operaciones CRUD de la clase Client.
    """
    queryset = Client.objects.all()  # Obtiene todos los clientes de la base de datos
    serializer_class = ClientSerializer  # Usa el serializador ClientSerializer para convertir los objetos Client en datos JSON

class ReservationViewSet(viewsets.ModelViewSet):
    """
    Vista para las operaciones CRUD de la clase Reservation.
    """
    queryset = Reservation.objects.all()  # Obtiene todas las reservas de la base de datos
    serializer_class = ReservationSerializer  # Usa el serializador ReservationSerializer para convertir los objetos Reservation en datos JSON

class RateViewSet(viewsets.ModelViewSet):
    """
    Vista para las operaciones CRUD de la clase Rate.
    """
    queryset = Rate.objects.all()  # Obtiene todas las tarifas de la base de datos
    serializer_class = RateSerializer  # Usa el serializador RateSerializer para convertir los objetos Rate en datos JSON

class AvailabilityViewSet(viewsets.ModelViewSet):
    """
    Vista para las operaciones CRUD de la clase Availability.
    """
    queryset = Availability.objects.all()  # Obtiene toda la disponibilidad de las habitaciones de la base de datos
    serializer_class = AvailabilitySerializer  # Usa el serializador AvailabilitySerializer para convertir los objetos Availability en datos JSON