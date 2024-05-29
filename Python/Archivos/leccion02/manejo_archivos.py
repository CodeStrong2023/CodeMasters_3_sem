# declaramos una variable
try:
    archivo= open("prueba.txt", "w", encoding='utf8')
    archivo.write("peogramamos con diferentes tipos de archivos, ahora en txt. \n")
    archivo.write("los acentos son importantes para las palabtas. \n")
    archivo.write("como por ejemplo: acción, ejecución y producción.\n")
    archivo.write("las letras son: \nr de read leer, \na append anexa, \nw write escribe, \nx crea archivos")
    archivo.write("\nt esta es para textos o text, \nb archivos binarios, \nw+ lee y escribe son iguales r+\n")
    archivo.write("Saludos a todos los alumnos de la tecnicatura\n")
    archivo.write("con esto terminamos")
except Exception as e:
    print(e)
finally:
    archivo.close()
    
# archivo.write("con esto terminamos") esto es un error
