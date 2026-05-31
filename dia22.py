import random

def generar_carton():
    numeros = random.sample(range(1, 31), 15)  # Genera 15 números únicos entre 1 y 30
    carton = [numeros[i:i+5] for i in range(0, 15, 5)]  # Crea una matriz de 3 filas x 5 columnas
    return carton

def mostrar_carton(carton):
    print("----- CARTÓN -----")
    for fila in carton:
        print(" ".join(f"{num:2}" for num in fila))

def sacar_bola(bolas_sacadas):
    while True:
        bola = random.randint(1, 30)
        if bola not in bolas_sacadas:
            bolas_sacadas.add(bola)
            return bola

def marcar_carton(carton, bola):
    for i in range(len(carton)):
        for j in range(len(carton[i])):
            if carton[i][j] == bola:
                carton[i][j] = 'X'
                return True
    return False

def comprobar_linea(carton):
    for fila in carton:
        if all(num == 'X' for num in fila):
            return True
    for columna in range(len(carton[0])):
        if all(carton[fila][columna] == 'X' for fila in range(len(carton))):
            return True
    return False

def comprobar_bingo(carton):
    for fila in carton:
        if any(num != 'X' for num in fila):
            return False
    return True

bolon_sacadas = set()
carton = generar_carton()
mostrar_carton(carton)
linea_conseguida = False
bolas_contadas_linea = 0
bolas_contadas_bingo = 0

while True:
    input("Pulsa Enter para sacar una bola...")
    bola = sacar_bola(bolon_sacadas)
    if not linea_conseguida:
        bolas_contadas_linea += 1
    bolas_contadas_bingo += 1
    print(f"Bola extraída: {bola}")

    if marcar_carton(carton, bola):
        print("¡Acierto!")
    else:
        print("No está en el cartón.")

    mostrar_carton(carton)

    if not linea_conseguida and comprobar_linea(carton):
        print("¡LÍNEA!")
        linea_conseguida = True

    if comprobar_bingo(carton):
        print("¡BINGO!")
        print(f"Has conseguido línea en {bolas_contadas_linea} bolas y bingo en {bolas_contadas_bingo} bolas.")
        break

