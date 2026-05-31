def solicitarNumero():
    while True:
        try:
            return int(input("Introduce un numero entero: "))
        except ValueError:
            print("Entrada invalida, intenta de nuevo.")

numeroUsuario = solicitarNumero()
print("Has introducido:", numeroUsuario)