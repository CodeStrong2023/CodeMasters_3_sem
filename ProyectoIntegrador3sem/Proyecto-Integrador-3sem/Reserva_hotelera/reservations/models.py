from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    # otros campos del cliente

class Reserva(models.Model):
    habitacion = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    # otros campos necesarios