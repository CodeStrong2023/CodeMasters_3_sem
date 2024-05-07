from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado('Lucia', 50000.00)
imprimir_detalles(empleado)

gerente = Gerente('Luciana', 60000.00, 'Sistemas')
imprimir_detalles(gerente)
