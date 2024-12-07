from psycopg2._psycopg import cursor

from capa_datos_persona.Persona import Persona
from capa_datos_persona.conexion import Conexion
import logging as log

class PersonaDao:
    """
    DAO significa: Data Access Objeto
    CRUD significa:
                    CREATE:  -> Insertar
                    READ:    -> Seleccionar
                    UPDATE:  -> Actualizar
                    DELETE:  -> Eliminar
    """

    _SELECCIONAR = 'SELECT * FROM persona ORDER by id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR =  'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    # Definimos los métodos
    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []  # Creamos una lista
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas

    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona insertada: {persona}')
                return cursor.rowcount


    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                log.debug(f'Persona insertada: {persona}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls.ELIMINAR, valores)
                log.debug(f'Los objetos eliminados son: {persona}')
                return cursor.rowcount

#if __name__ == '__main__':
#    #Actualizar un registro
#    persona1 = Persona(1, 'Juan Jose', 'Pena', 'jjpena@gmail.com')
#    personas_actualizadas = PersonaDao.actualizar(persona1)
#   log.debug(f'Personas Actualizadas: {personas_actualizadas}')

if __name__ == '__name__':
    #Eliminar un registro
    persona1 = Persona(id_persona=13)
    personas_eliminadas = PersonaDao.eliminar(persona1)
    log.debug(f'Personas elimnadas: {personas_eliminadas}')

#if __name__ == '__main__':
#    #Insertar un registro
#    persona1 = Persona(nombre='Pedro', apellido='Romero', email='promero@mail.com')
#    personas_insertadas = PersonaDao.insertar(persona1)
#    log.debug(f'Personas insertadas: {personas_insertadas}')

#    #seleccionar objetos
#    personas = PersonaDao.seleccionar()
#    for personas in personas:
#        log.debug(personas)
