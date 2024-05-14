class NumerosIgualesException(Exception): # Se estirnde de la clase
    def __init__(self, mensaje):
        self.message = mensaje