from django.db import models

class Room(models.Model):
    """
    Representa una habitación en el hotel.
    """
    ROOM_TYPE_CHOICES = [
        ('SINGLE', 'Individual'),
        ('DOUBLE', 'Doble'),
        ('SUITE', 'Suite'),
    ]
    type = models.CharField(max_length=10, choices=ROOM_TYPE_CHOICES)
    capacity = models.IntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_type_display()} - Capacidad: {self.capacity}"

    class Meta:
        verbose_name = "Habitación"
        verbose_name_plural = "Habitaciones"
        ordering = ['type', 'capacity']


class Client(models.Model):
    """
    Representa un cliente que puede reservar una habitación.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['last_name', 'first_name']



class Reservation(models.Model):
    """
    Representa una reserva realizada por un cliente.
    """
    STATUS_CHOICES = [
        ('BOOKED', 'Reservado'),
        ('CANCELLED', 'Cancelado'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='reservations')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reserva {self.id} - {self.client} - {self.room}"

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ['check_in_date', 'status']


class Rate(models.Model):
    """
    Representa tarifas estacionales para habitaciones.
    """
    SEASON_CHOICES = [
        ('LOW', 'Baja'),
        ('HIGH', 'Alta'),
        ('PEAK', 'Pico'),
    ]
    season = models.CharField(max_length=10, choices=SEASON_CHOICES)
    rate_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Temporada {self.get_season_display()} - Tarifa: {self.rate_per_night}"

    class Meta:
        verbose_name = "Tarifa"
        verbose_name_plural = "Tarifas"
        ordering = ['season']


class Availability(models.Model):
    """
    Representa la disponibilidad de una habitación para una fecha específica.
    """
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='availabilities')
    date = models.DateField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.room} - Fecha: {self.date} - Disponible: {self.is_available}"

    class Meta:
        verbose_name = "Disponibilidad"
        verbose_name_plural = "Disponibilidades"
        ordering = ['date']
        unique_together = ['room', 'date']
