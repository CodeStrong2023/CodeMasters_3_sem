from ManejoArchivo import ManejoArchivos

# Manejo de contexto with
# with open('prueba.txt', 'r', encoding='utf8') as archivo:
  #  print(archivo.read())

# No hace falta try ni finally
# Utiliza diferentes métodos: __enter__ (abre) __exit__ (cierra)

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())

