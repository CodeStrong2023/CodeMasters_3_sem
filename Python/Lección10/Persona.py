class Persona:
    contador_personas = 0 # variable de clase

    @classmethod
    def generar_sigiente_valor(cls):
        cls.contador_personas += 1 # Incremento
        return cls.contador_personas

    def __init__(self, nombre, edad):
        # Persona.contador_personas += 1 # incremento
        self.id_persona = Persona.generar_sigiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona [{self.id_persona} = {self.nombre} {self.edad}]"

persona1 = Persona("Luciana", 23)
print(persona1)
persona2 = Persona("Lucia", 23)
print(persona2)
persona3 = Persona("Nacho", 23)
print(persona3)

Persona.generar_sigiente_valor()

persona4 = Persona("Pablo", 23)
print(persona4)

print(f"Valor del contador de personas: {Persona.contador_personas}")
