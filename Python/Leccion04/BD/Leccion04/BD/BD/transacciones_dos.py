import psycopg2 as bd #Esto es para conectarnos a postgre

conexion = bd.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
try:
    conexion.autocommit = False # true no es una buena practica
    cursor = conexion.cursor()
    sentencia = "INSERT INTO persona(nombre, apellido, email)VALUES (%s, %s, %s)"
    valores = ("Jorge", "Prol", "jprol@gmail.com")
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores =("Juan", "Juarez", "jcjuares@gmail.com", 1)
    cursor.execute(sentencia, valores)

    conexion.commit() # Hacemos el commit manualmente
    print("Termina la transacción")
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo un rollback: {e}')
finally:
    conexion.close()