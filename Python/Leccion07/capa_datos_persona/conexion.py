from psycopg2 import pool
from logger_base import log
import sys

class Conexion:
    _DATABASE = 'test_bd'
    _USERNAME = 'postgres'
    _PASSWORD = 'root'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MINCON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion



    @classmethod
    def obtenerPool(cls):
        if cls.pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MINCON,
                                                      cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                log.debug(f'creacion dedl pool exitosa: {cls._pool}')
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la coneion del pool: {conexion}')


if __name__ == '__main__':
   conexion1 = Conexion.obtenerConexion()
   Conexion.liberarConexion(conexion1)
   conexion2 = Conexion.obtenerConexion()
   Conexion.liberarConexion(conexion2)
   conexion4 = Conexion.obtenerConexion()
   Conexion.liberarConexion(conexion4)
   conexion5 = Conexion.obtenerConexion()
   Conexion.liberarConexion(conexion5)