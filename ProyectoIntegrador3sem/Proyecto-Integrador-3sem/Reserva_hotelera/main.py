from database import (
    realizar_reserva,
    cancelar_reserva,
    verificar_disponibilidad,
    actualizar_disponibilidad,
    generar_factura
)

# Realizar una reserva (asegúrate de usar un ID de cliente y habitación válidos)
print("Realizando una nueva reserva...")
realizar_reserva(1, 2, '2024-07-01 14:00:00', '2024-07-05 12:00:00', 'Confirmada')

# Generar factura para la reserva creada
#print("Generando factura para la reserva...")
factura = generar_factura(1)  # Asegúrate de usar el ID correcto de la reserva recién creada
if factura:
    for key, value in factura.items():
        print(f"{key}: {value}")

# Verificar disponibilidad (opcional)
#print("Verificando disponibilidad...")
disponible = verificar_disponibilidad(1, '2024-07-01')
#print(f"Disponibilidad: {'Sí' if disponible else 'No'}")

# Actualizar disponibilidad (opcional)
#print("Actualizando disponibilidad...")
actualizar_disponibilidad(1, '2024-07-01', 'Ocupada')

# Cancelar reserva (opcional)
# print("Cancelando reserva...")
# cancelar_reserva(1)