import psycopg2 as bd #Esto es para conectarnos a postgre

conexion = bd.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
# Esta es la mejor practica, que se realize de manera automatica
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "INSERT INTO persona(nombre, apellido, email)VALUES (%s, %s, %s)"
            valores = ("Alex", "Rojas", "alexro@gmail.com")
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores =("Juan", "Del potro", "juanmartindp@gmail.com", 1)
            cursor.execute(sentencia, valores)

except Exception as e:
    print(f'Ocurrio un error, se hizo un rollback: {e}')
finally:
    conexion.close()

print("Termina la transacción")