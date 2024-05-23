# Se imprime el mensaje de bienvenida
print("")
print("Bienvenidos al Sistema de Reservas")
print("")

# Se define una función para centrar el titulo
def centrar_titulo(titulo):
    longitud_total = 80  # Longitud total de la línea
    espacios_alrededor = (longitud_total - len(titulo)) // 2
    titulo_centrado = titulo.center(longitud_total)
    return titulo_centrado

# Se define el nombre del hotel
titulo = "HOTEL MENDOZA"
titulo_centrado = centrar_titulo(titulo)
print(titulo_centrado)
print("")

# Se define la clase habitación
class Habitacion:
    def __init__(self, numero, tipo, precio, disponible=True):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = disponible

# Se define la clase cliente
class Cliente:
    print("")
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

# Definimos una función para registrar un cliente        
def registrar_cliente():
    print("")
    print("Por favor, ingresá tus datos:")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = input("Email: ")
    print("")
    return Cliente(nombre, apellido, email)   

# Definimos una clase hotel
class Hotel:
    def __init__(self, nombre, habitaciones):
        self.nombre = nombre
        self.habitaciones = habitaciones
        self.reservas = []

    # Creamos una función para mostrar las habitaciones que se encuentran disponibles
    def mostrar_habitaciones_disponibles(self):
        print("Habitaciones disponibles:")
        for habitacion in self.habitaciones:
            if habitacion.disponible:
                print(f"Número: {habitacion.numero}, Tipo: {habitacion.tipo}, Precio: ${habitacion.precio}")
        print("")
    # Definimos una función para la selección de la habitación que se encuentren disponibles, con un ciclo while
    def seleccionar_habitacion(self):
        while True:
            self.mostrar_habitaciones_disponibles()
            seleccion = input("Selecciona el número de la habitación que deseas: ")
        
            try:
                seleccion = int(seleccion)
                for habitacion in self.habitaciones:
                    if habitacion.numero == seleccion and habitacion.disponible:
                        return habitacion
            except ValueError:
                print("Por favor, ingresa un número válido.")            

            salir = input("presiona 'q' para salir:")
            if salir.lower()=='q':
                return None

    # Definimos una función para crear una reserva
    def hacer_reserva(self, cliente, habitacion, fecha_inicio, fecha_fin):
        if habitacion:
            reserva = Reserva(cliente, habitacion,fecha_inicio, fecha_fin)
            self.reservas.append(reserva)
            habitacion.disponible = False
            print("")
            print("Reserva realizada con éxito.")
            print("")
            return True
        else:
            print("Lo sentimos, no hay disponibilidad para ese tipo de habitación.")
            print("") 
            return False   

# Creamos una clase para Reserva
class Reserva:
    def __init__(self, cliente, habitacion, fecha_inicio, fecha_fin):
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin          

# creamos una variable, donde se muestran una lista con las habitaciones del hotel             
habitaciones_hotel = [
    Habitacion(numero=101, tipo="individual", precio=50),
    Habitacion(numero=102, tipo="individual", precio=50),
    Habitacion(numero=201, tipo="doble", precio=80),
    Habitacion(numero=202, tipo="doble", precio=80)
    ]

# Creamos una instanciadel hotel con la lista de habitaciones
hotel_ejemplo = Hotel(nombre="Hotel Mendoza", habitaciones=habitaciones_hotel)



#Registro del cliente
nuevo_cliente = registrar_cliente()
print("\nCliente registrado:")
print(f"Nombre: {nuevo_cliente.nombre}")
print(f"Apellido: {nuevo_cliente.apellido}")
print(f"Email: {nuevo_cliente.email}")
print("")

# Selección de habitación y reserva
habitacion_seleccionada = hotel_ejemplo.seleccionar_habitacion()
if habitacion_seleccionada:
    print("\nHas seleccionado la habitación:")
    print(f"Número: {habitacion_seleccionada.numero}, Tipo: {habitacion_seleccionada.tipo}, Precio: ${habitacion_seleccionada.precio}")
    fecha_inicio = input("Ingresa la fecha de inicio de la reserva (YYYY-MM-DD): ")
    fecha_fin = input("Ingresa la fecha de fin de la reserva (YYYY-MM-DD): ")
    hotel_ejemplo.hacer_reserva(nuevo_cliente, habitacion_seleccionada, fecha_inicio, fecha_fin)
else:
    print("No se seleccionó ninguna habitación")
print("")







    







    

