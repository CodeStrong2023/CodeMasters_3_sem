class MiClase:
    # Variable de clase.eeste atributo dará a cada objeto el mismo valor
    variable_clase = 'Esta es una variable de clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico(): #Metodo estatico
        print(MiClase.variable_clase)

print(MiClase.variable_clase)
miClase1 = MiClase('Esta es una variable de instancia')
print(miClase1.variable_instancia)
print(miClase1.variable_clase)
miClase2 = MiClase('Esta es una prueba de variables')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)

MiClase.variable_clase2 = "Valor de la variable de clase 2"
print(MiClase.variable_clase2)
print(miClase1.variable_clase2)
print(miClase2.variable_clase2)

MiClase.metodo_estatico()

