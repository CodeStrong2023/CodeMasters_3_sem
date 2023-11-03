def calcular_total_pago(pago_sin_impuestos, impuesto):
     pago_total = pago_sin_impuestos + pago_sin_impuestos * (impuesto/100)
     return pago_total

#Ejecutamos la función
pago_sin_impuesto = float(input('Digite el pago sin impuestos'))
impuesto = float(input('Digite el monto del impuesto a pagar '))

pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'El pago con impuesto es : {pago_con_impuesto} ')