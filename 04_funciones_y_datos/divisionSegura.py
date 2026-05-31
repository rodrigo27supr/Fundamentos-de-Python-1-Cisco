try:
    divisor = int(input("Introduce un numero para dividir 100: "))
    resultado = 100 / divisor
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Error: No puedes dividir entre cero.")
except ValueError:
    print("Error: Debes introducir un numero valido.")