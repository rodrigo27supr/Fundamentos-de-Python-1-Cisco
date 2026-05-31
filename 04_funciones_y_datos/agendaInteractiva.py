agenda = {}

def agregarContacto(nombre, telefono):
    agenda[nombre] = telefono

def buscarContacto(nombre):
    return agenda.get(nombre, "No existe")

while True:
    accion = input("1. Agregar, 2. Buscar, 3. Salir: ")
    if accion == "1":
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        agregarContacto(nombre, telefono)
    elif accion == "2":
        nombre = input("Nombre a buscar: ")
        print(buscarContacto(nombre))
    elif accion == "3":
        break