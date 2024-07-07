from django.db import models
from django import forms

# Create your models here.

class Chambre(models.Model):
    nom = models.CharField(max_length=20)
    prix = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='media/pics')
    disponibilité = models.BooleanField(default=True)

    def __str__(self):
        return self.nom

class Catalogue(models.Model):
    image = models.ImageField(upload_to='pics')

class Testimonial(models.Model):
    nom = models.CharField(max_length=20)
    avis = models.TextField()
    image = models.ImageField(upload_to='media/pics')

    def __str__(self):
        return self.nom

class Reservation(models.Model):
    Name = models.CharField(max_length=20)
    Phone = models.BigIntegerField(default=0)
    Email = models.EmailField(max_length=40)
    Date_Check_In = models.DateField()
    Date_Check_Out = models.DateField()
    Adulte = models.IntegerField()
    Children = models.IntegerField(default=0)
    Note = models.TextField(blank=True, null=True)  # Notes can be optional

    def __str__(self):
        return self.Name

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['Name', 'Phone', 'Email', 'Date_Check_In', 'Date_Check_Out', 'Adulte', 'Children', 'Note']