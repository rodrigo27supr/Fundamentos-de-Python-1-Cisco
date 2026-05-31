numeroParaFactorial = int(input("Introduce un numero positivo: "))
resultadoFactorial = 1

for contadorActual in range(1, numeroParaFactorial + 1):
    resultadoFactorial = resultadoFactorial * contadorActual

print("El factorial de", numeroParaFactorial, "es:", resultadoFactorial)