# Ejercicio 4: Calculadora de impuestos
# crear una funcion para calcular el total de un pago incluyendo
# un impuestp aplicado (iva)
# formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
# proporsione el pago sin impuesto: 1000
# proporcione el monto del impuesto 21%
# pago con impuesto: XXXXX

def calculadora_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

# ejecutamos la funcio
pago_sin_impuesto = float(input('Ingrese el pago sin impuesto: '))
impuesto = float(input('Ingrese el monto de impuesto a aplicar: '))
pago_con_impuesto = calculadora_total_pago(pago_sin_impuesto, impuesto)
print(f'El pago con impuesto es: {pago_con_impuesto}')
