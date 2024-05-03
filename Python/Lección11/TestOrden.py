from Orden import Orden
from Producto import Producto


producto1 = Producto('Camiseta', 100.00)
producto2 = Producto('Pantalon', 150.00)
producto3 = Producto('Campera', 250.00)
producto4 = Producto('Zapatillas Adidas', 345.00)
producto5 = Producto('Remera', 180.00)
producto6 = Producto('Camisa Yean', 450.00)

productos1 = [producto1, producto2]  # Lista de productos
orden1 = Orden(productos1) # Primer objeto orden pasando la lista de productos
orden1.agregar_producto(producto6)
orden1.agregar_producto(producto5)
print(orden1)
print(f'total de la orden 1: {orden1.calcular_total()}')
productos2 = [producto3, producto4]
orden2 = Orden(productos2)
print(orden2)
print(f'total de la orden 2: {orden2.calcular_total()}')
