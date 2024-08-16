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
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'#Placeholder
            entrada = input('Digite los id_personas a buscar(separados por comas): ')
            llaves_primarias = (tuple(entrada.split(', ')),)
            cursor.execute(sentencia, llaves_primarias)# De esta manera ejecutamos la sentencia
            registros = cursor.fetchall()#Recuperamos todos los registros que serán una lista
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()