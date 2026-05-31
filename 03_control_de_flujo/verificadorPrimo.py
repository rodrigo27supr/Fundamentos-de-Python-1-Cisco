numeroIngresado = int(input("Introduce un numero mayor a 1: "))
esPrimo = True

for divisorActual in range(2, numeroIngresado):
    if numeroIngresado % divisorActual == 0:
        esPrimo = False
        break

if esPrimo:
    print("El numero es primo")
else:
    print("El numero no es primo")