saldoActual = 1000
opcionSeleccionada = 0

while opcionSeleccionada != 3:
    print("\n1. Ver saldo")
    print("2. Retirar dinero")
    print("3. Salir")
    opcionSeleccionada = int(input("Elige una opcion: "))

    if opcionSeleccionada == 1:
        print("Tu saldo es:", saldoActual)
    elif opcionSeleccionada == 2:
        retiro = int(input("Cantidad a retirar: "))
        if retiro <= saldoActual:
            saldoActual = saldoActual - retiro
        else:
            print("Saldo insuficiente")