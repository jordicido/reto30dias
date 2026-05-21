import random

saldo = 10
simbolos = ["🍒","🍒","🍒","🍋","🍋","🍋","🔔","🔔","🔔","⭐","💵","💵","💎","💎"]
partidas = 0
victorias = 0

while True:
    print(f"""
----- TRAGAPERRAS -----

1. Jugar partida
2. Añadir saldo
3. Ver saldo
4. Salir
          """)
    opcion = int(input("Introduce la opción deseada: "))
    if opcion == 1:
        if saldo <= 0:
            print("No tienes saldo suficiente")
            continue
        
        partidas += 1
        saldo -= 1
        tirada = []
        for i in range(3):
            tirada.append(simbolos[random.randint(0,13)])

        print(tirada)
        if tirada[0] == tirada[1] == tirada[2]:
            if tirada[0] == "⭐":
                print("Jackpot especial! Ganas 25 monedas")
                saldo += 25
            else:
                print("Jackpot! Ganas 10 monedas")
                saldo += 10
            print(f"Saldo actual: {saldo} monedas")    
            victorias += 1
        elif tirada[0] == tirada[1] or tirada[1] == tirada[2] or tirada[0] == tirada[2]:
            if tirada.count("💵") == 2 or tirada.count("💎") == 2:
                print("Premio menor especial! Ganas 5 monedas")
                saldo += 5
            else:
                print("Premio menor! Ganas 3 monedas")
                saldo += 3
            print(f"Saldo actual: {saldo} monedas")
            victorias += 1
        else:
            print("1, 2, 3 avance, sigue intentandolo")

        print(f"Has jugado {partidas} partidas y has ganado {victorias} veces")
    elif opcion == 2:
        saldo_a_anadir = int(input("Introduce el saldo a añadir: "))
        saldo += saldo_a_anadir
    elif opcion == 3:
        print(f"Saldo actual: {saldo} monedas")
    if opcion == 4:
        print("Volverás")
        break