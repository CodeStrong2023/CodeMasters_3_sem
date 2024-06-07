import psycopg2 #esto es para poder conectarse a Postgre

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    database='test_db'
)

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia) # de esta menera ejecutamos la sentencia
registros = cursor.fetchall() #Recuperamos todos los registros que seran una lista
print(registros)

cursor.close()
conexion.close()