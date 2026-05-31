numeroBase = int(input("Introduce un numero para ver su tabla: "))

for multiplicadorActual in range(1, 11):
    resultadoMultiplicacion = numeroBase * multiplicadorActual
    print(numeroBase, "x", multiplicadorActual, "=", resultadoMultiplicacion)