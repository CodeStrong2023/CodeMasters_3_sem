class Persona: #creamps una clase
    def __init__(self, nombre, apellido, edad): # se lo llama inir Deunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


persona1 = Persona('Julieta', 'Aguilera', 20)
print(f'El objeto1 de la clase Persona: {persona1.nombre} {persona1.apellido} y su esas es: {persona1.edad}')

persona2 = Persona('Eica', 'Murie', 19)
print(f'El objeto2 de la clase Persona: {persona2.nombre} {persona2.apellido} y su esas es: {persona2.edad}')

persona1.nombre = 'Rosalia'
persona1.apellido = 'Albaro'
persona1.edad = 22
print(f'El objeto1 modificado de la clase Persona: {persona1.nombre} {persona1.apellido} y su esas es: {persona1.edad}')

# Los atributos son: caracteristicas
# Los metodos son el comportamiendo que van tener los objetos (acciones)

persona1.mostrar_detalle()
persona2.mostrar_detalle()
