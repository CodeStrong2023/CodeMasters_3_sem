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
            sentencia = 'INSERT INTO persona (nombre, apellido, email)VALUES (%s, %s, %s)'
            valores = (
                ('Carlos', 'Lara', 'clar@gmail.com'),
                ('Marcos', 'Canto', 'mcanto@gmail.com'),
                ('Marcelo', 'Cuenca', 'CuencaM@gmail.com'))#Los introducimos como tupla
            cursor.executemany(sentencia, valores)# De esta manera ejecutamos la sentencia
            #conexion.commit()esto se utiliza para guardar los cambios en la base de datos
            registros_insertados = cursor.rowcount
            print(f'Los registros insertados son: {registros_insertados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()