# Calcular estación del año
mesdeano = int(input("Ingrese un mes del año entre el mes 1 y el mes 12:"))
estacion = None
if mesdeano == 1 or mesdeano == 2 or  mesdeano == 3:
     estacion = 'verano'
elif mesdeano == 4 or mesdeano == 5 or 6:
     estacion = 'otoño'
elif mesdeano == 7 or mesdeano == 8 or 9:
     estacion = 'invierno'
elif mesdeano == 10 or mesdeano == 11 or 12:
     estacion = 'primavera'
else:
     estacion = 'Error no hay número para ese mes'
print(f'usted está en el{mesdeano}  en la estación: {estacion} ')

