def calcularEstadisticas(listaNumeros):
    sumaTotal = sum(listaNumeros)
    cantidadElementos = len(listaNumeros)
    promedio = sumaTotal / cantidadElementos
    return (sumaTotal, promedio)

resultados = calcularEstadisticas([10, 20, 30, 40])
print("Suma:", resultados[0], "Promedio:", resultados[1])