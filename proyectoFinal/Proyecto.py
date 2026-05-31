from random import randrange


def mostrar_tablero(tablero):
    print("+-------" * 3, "+", sep="")
    for fila in range(3):
        print("|       " * 3, "|", sep="")
        for columna in range(3):
            print("|   " + str(tablero[fila][columna]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def ingresar_movimiento(tablero):
    valido = False
    while not valido:
        movimiento = input("Ingresa tu movimiento: ")
        valido = len(movimiento) == 1 and movimiento >= '1' and movimiento <= '9'
        if not valido:
            print("Movimiento erróneo, ingrésalo nuevamente")
            continue

        indice = int(movimiento) - 1
        fila = indice // 3
        columna = indice % 3
        marca = tablero[fila][columna]
        valido = marca not in ['O', 'X']
        if not valido:
            print("¡Cuadro ocupado, ingresa nuevamente!")
            continue

    tablero[fila][columna] = 'O'


def obtener_lista_de_campos_libres(tablero):
    libres = []
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] not in ['O', 'X']:
                libres.append((fila, columna))
    return libres


def verificar_victoria(tablero, simbolo):
    if simbolo == "X":
        ganador = 'me'
    elif simbolo == "O":
        ganador = 'you'
    else:
        ganador = None

    diagonal_principal = True
    diagonal_secundaria = True

    for indice in range(3):
        if tablero[indice][0] == simbolo and tablero[indice][1] == simbolo and tablero[indice][2] == simbolo:
            return ganador
        if tablero[0][indice] == simbolo and tablero[1][indice] == simbolo and tablero[2][indice] == simbolo:
            return ganador
        if tablero[indice][indice] != simbolo:
            diagonal_principal = False
        if tablero[indice][2 - indice] != simbolo:
            diagonal_secundaria = False

    if diagonal_principal or diagonal_secundaria:
        return ganador
    return None


def realizar_movimiento_maquina(tablero):
    libres = obtener_lista_de_campos_libres(tablero)
    cantidad = len(libres)
    if cantidad > 0:
        eleccion = randrange(cantidad)
        fila, columna = libres[eleccion]
        tablero[fila][columna] = 'X'


tablero = [[3 * fila + columna + 1 for columna in range(3)] for fila in range(3)]
tablero[1][1] = 'X'
libres = obtener_lista_de_campos_libres(tablero)
turno_humano = True

while len(libres):
    mostrar_tablero(tablero)
    if turno_humano:
        ingresar_movimiento(tablero)
        victorioso = verificar_victoria(tablero, 'O')
    else:
        realizar_movimiento_maquina(tablero)
        victorioso = verificar_victoria(tablero, 'X')

    if victorioso is not None:
        break

    turno_humano = not turno_humano
    libres = obtener_lista_de_campos_libres(tablero)

mostrar_tablero(tablero)
if victorioso == 'you':
    print("¡Has ganado!")
elif victorioso == 'me':
    print("¡He ganado!")
else:
    print("¡Empate!")