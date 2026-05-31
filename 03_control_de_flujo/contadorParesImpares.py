cantidadNumeros = 5
contadorPares = 0
contadorImpares = 0

for iteracionActual in range(cantidadNumeros):
    numeroIngresado = int(input("Introduce un numero: "))
    if numeroIngresado % 2 == 0:
        contadorPares = contadorPares + 1
    else:
        contadorImpares = contadorImpares + 1

print("Total pares:", contadorPares)
print("Total impares:", contadorImpares)