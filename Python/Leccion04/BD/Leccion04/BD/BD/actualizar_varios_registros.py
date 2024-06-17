import psycopg2 #Esto es para conectarnos a postgre

conexion = psycopg2.connect(
    user='mis_servers',
    password='laujaz1706',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (('Juan ', 'Perez', 'jPer@gmail', 4),
            ('Romina', 'Rodriguez', 'romi@gmail.com', 5))
            cursor.executemany(sentencia, valores)# De esta manera ejecutamos la sentencia
            registros_actualizados = cursor.rowcount
            print(f'Los registros actualizados son: {registros_actualizados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()