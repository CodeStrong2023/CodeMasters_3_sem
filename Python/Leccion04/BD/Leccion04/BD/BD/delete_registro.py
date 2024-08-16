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
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Digite los números de registros a elimina(separados por comas): ')
            valores = (entrada)#es una tupla de valores
            cursor.execute(sentencia, valores)# De esta manera ejecutamos la sentencia
            registros_eliminados = cursor.rowcount
            print(f'Los registros eliminados son: {registros_eliminados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()