import logging as log

# Configurar logging para que los mensajes se registren en el archivo capa_datos.log
log.basicConfig(
    filename='capa_datos.log',  # Nombre del archivo de log
    level=log.DEBUG,            # Nivel de logging que deseas capturar (DEBUG es el más detallado)
    format='%(asctime)s:%(levelname)s:%(message)s',  # Formato del mensaje de log
    datefmt='%Y-%m-%d %H:%M:%S'  # Formato de la fecha/hora
)

class Persona:
    def __init__(self, id_persona, nombre, apellido, email):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self):
        return f'''
            Id Persona: {self._id_persona};
            Nombre: {self._nombre},
            Apellido: {self._apellido},
            Email: {self._email}
        '''

    # Métodos Getters and Setters
    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email


if __name__ == '__main__':
    persona1 = Persona(1, 'Juan', 'Perez', 'jperez@gmail.com')
    log.debug(persona1)
    persona2 = Persona(2, 'Jose', 'Lopez', 'ljose@gmail.com')
    log.debug(persona2)
