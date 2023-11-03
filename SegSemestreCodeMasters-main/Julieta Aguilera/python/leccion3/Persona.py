class Persona: # creamos una clase
    def __init__(self, nombre, apellido, edad): # se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona('Julieta', 'Aguilera', '20') # necesitamos enviar argumentos

print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona1 = Persona('Julieta','Aguilera', 20)
print(f'El objeto 1 de la clase Persona es: {persona1.nombre}, {persona1.apellido}, Su edad es: {persona1.edad}')
persona2 = Persona('Rocio', 'Albaro', 22)
print(f'El objeto 2 de la clase persona: {persona2.nombre}, {persona2.apellido}, Su edad es: {persona2.edad}')
