import psycopg2 # Con esto se conecta a Postgre

conexion = psycopg2.connect(
    user="postgres",
    password="admin",
    host="127.0.0.1",
    port="5432",
    database="test_bd"
)

# print(conexion)

cursor = conexion.cursor()
sentencia = "SELECT * FROM persona"
cursor.execute(sentencia) #Ejecutamos la sentencia
registro = cursor.fetchall() #Recuperamos todos los registros que serán una lista

print(registro)

cursor.close()
conexion.close()