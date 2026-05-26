import random

def generar_tesoro():
    fila = random.randint(1, 8)
    columna = random.randint(1, 8)
    return fila, columna

def mostrar_mapa(tesoro_fila, tesoro_columna, intentos, encontrado):
    for fila in range(1, 9):
        for columna in range(1, 9):
            if (fila, columna) == (tesoro_fila, tesoro_columna) and encontrado:
                print('X', end=' ')
            elif (fila, columna) in intentos:
                print('O', end=' ')
            else:
                print('.', end=' ')
        print()

def obtener_coordenadas():
    while True:
        try:
            fila = int(input("Introduce la fila (1-8): "))
            columna = int(input("Introduce la columna (1-8): "))
            if 1 <= fila <= 8 and 1 <= columna <= 8:
                return fila, columna
            else:
                print("Coordenadas fuera de rango. Intenta de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce números.")

intentos = []
tesoro_fila, tesoro_columna = generar_tesoro()
encontrado = False
contador_intentos = 0

while not encontrado:
    mostrar_mapa(tesoro_fila, tesoro_columna, intentos, encontrado)
    fila, columna = obtener_coordenadas()
    contador_intentos += 1

    if (fila, columna) == (tesoro_fila, tesoro_columna):
        encontrado = True
        print(f"¡Has encontrado el tesoro! Intentos realizados: {contador_intentos}")
        mostrar_mapa(tesoro_fila, tesoro_columna, intentos, encontrado)
    else:
        intentos.append((fila, columna))
        print("No has encontrado el tesoro.")
        if fila < tesoro_fila:
            print("El tesoro está más abajo.")
        elif fila > tesoro_fila:
            print("El tesoro está más arriba.")
        if columna < tesoro_columna:
            print("El tesoro está más a la derecha.")
        elif columna > tesoro_columna:
            print("El tesoro está más a la izquierda.")

    if contador_intentos >= 10:
        print("¡Has alcanzado el límite de intentos! El tesoro estaba en:")
        print(f"Fila: {tesoro_fila}, Columna: {tesoro_columna}")
        mostrar_mapa(tesoro_fila, tesoro_columna, intentos, encontrado)
        break