import random

def generar_barcos():
    orientacion = random.choice(['horizontal', 'vertical'])
    barcos = []
    if orientacion == 'horizontal':
        fila = random.randint(1, 6)
        columna = random.randint(1, 4)  # Para que no se salga del tablero
        barcos.append([(fila, columna), (fila, columna + 1), (fila, columna + 2)])
    else:
        fila = random.randint(1, 4)  # Para que no se salga del tablero
        columna = random.randint(1, 6)
        barcos.append([(fila, columna), (fila + 1, columna)])
    
    orientacion = random.choice(['horizontal', 'vertical'])
    if orientacion == 'horizontal':
        fila = random.randint(1, 6)
        columna = random.randint(1, 5)
        while (fila, columna) in barcos[0] or (fila, columna + 1) in barcos[0]:
            fila = random.randint(1, 6)
            columna = random.randint(1, 5)
        barcos.append([(fila, columna), (fila, columna + 1)])
    else:
        fila = random.randint(1, 5) 
        columna = random.randint(1, 6)
        while (fila, columna) in barcos[0] or (fila + 1, columna) in barcos[0]:
            fila = random.randint(1, 5)
            columna = random.randint(1, 6)
        barcos.append([(fila, columna), (fila + 1, columna)])

    return barcos

    
def mostrar_tablero(barcos, disparos):
    for fila in range(1, 7):
        for columna in range(1, 7):
            if (fila, columna) in barcos[0] and (fila, columna) in disparos:
                print('X', end=' ')
            elif (fila, columna) in barcos[1] and (fila, columna) in disparos:
                print('X', end=' ')
            elif (fila, columna) in disparos:
                print('O', end=' ')
            else:
                print('~', end=' ')
        print()

def obtener_coordenadas():
    while True:
        try:
            fila = int(input("Introduce la fila (1-6): "))
            columna = int(input("Introduce la columna (1-6): "))
            if 1 <= fila <= 6 and 1 <= columna <= 6:
                return fila, columna
            else:
                print("Coordenadas fuera de rango. Intenta de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce números.")

barcos = generar_barcos()
disparos = []
intentos = 0
partes_tocadas = 0
contador_disparos = 0

while partes_tocadas < 5 and contador_disparos < 12:
    mostrar_tablero(barcos, disparos)
    fila, columna = obtener_coordenadas()
    contador_disparos += 1

    if (fila, columna) in disparos:
        print("Ya habías disparado ahí. Prueba otra coordenada.")
        continue
    
    disparos.append((fila, columna))
    intentos += 1
    
    if (fila, columna) in barcos[0] or (fila, columna) in barcos[1]:
        partes_tocadas += 1
        if partes_tocadas == 5:
            print("¡Tocado y hundido!")
        else:
            print("¡Tocado!")
    else:
        print("Agua.")

    print(f"Partes restantes: {5 - partes_tocadas}")
    
if partes_tocadas == 5:
    print(f"Has hundido el barco. Intentos realizados: {intentos}")
else:
    print("Te has quedado sin disparos. El barco escapó.")