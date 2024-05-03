class Producto:
    contador_producto = 0 #variable de la clase

    def __init__(self, nombre, precio):
        Producto.contador_producto += 1 #aumento para la variable de clase
        self._id_producto = Producto.contador_producto #asignación desde la variable de clase
        self._nombre = nombre
        self._precio = precio

    # Métodos setters and getters
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    # Sobre escribimos el método srt
    def __str__(self):
        return f"ID Producto: {self._id_producto}, Nombres: {self._nombre}, precio: {self._precio}"

if __name__ == '__main__': # Sólo sera visible si la prueba se ejecuta desde aquí
    producto1 = Producto('Camiseta', 100.00)
    print(producto1)
    producto2 = Producto('Pantalon', 150.00)
    print(producto2)
    producto3 = Producto('Campera', 250.00)
    producto4 = Producto('Zapatillas Adidas', 345.00)
