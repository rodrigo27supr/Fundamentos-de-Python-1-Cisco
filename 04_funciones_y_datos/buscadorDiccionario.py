def obtenerTelefono(agenda, nombre):
    return agenda.get(nombre, "Contacto no encontrado")

misContactos = {"Aida": "600111222", "Betti": "600555666"}
print(obtenerTelefono(misContactos, "Betti"))