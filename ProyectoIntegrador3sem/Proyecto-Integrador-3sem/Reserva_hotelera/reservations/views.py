# reservations/views.py
from django.shortcuts import render, redirect
from .models import Reserva, Cliente

def crear_reserva(request):
    if request.method == 'POST':
        # Procesar los datos del formulario y crear una nueva reserva
        cliente_id = request.POST.get('cliente_id')
        habitacion = request.POST.get('habitacion')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        
        cliente = Cliente.objects.get(id=cliente_id)
        Reserva.objects.create(cliente=cliente, habitacion=habitacion, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)
        return redirect('crear_reserva')
    else:
        clientes = Cliente.objects.all()
        return render(request, 'crear_reserva.html', {'clientes': clientes})