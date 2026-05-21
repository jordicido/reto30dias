import random

game_mode = input("Elige la dificultad (1, 2 o 3): ")
if game_mode == "1":
    oxygen = 120
    food = 100
    energy = 80
elif game_mode == "2":
    oxygen = 100
    food = 80
    energy = 60
elif game_mode == "3":
    oxygen = 80
    food = 60
    energy = 40
else:
    print("Opción no válida. Se establecerá la dificultad normal.")
    oxygen = 100
    food = 80
    energy = 60

for day in range(1, 8):
    print(f"----- DÍA {day} -----")
    print(f"Oxígeno: {oxygen}")
    print(f"Comida: {food}")
    print(f"Energía: {energy}")

    action = input("Elige una acción (1, 2 o 3): ")
    
    if action == "1":
        food += 20
        energy -= 15
        oxygen -= 5
        print("Has encontrado suministros de comida.")
    elif action == "2":
        energy -= 20
        oxygen += 10
        food -= 5
        print("Has reparado parte del sistema de oxígeno.")
    elif action == "3":
        energy += 15
        food -= 10
        oxygen -= 5
        print("Has descansado y recuperado energía.")
    else:
        print("Opción no válida. No se ha realizado ninguna acción.")

    event = random.randint(1, 4)

    if event == 1:
        oxygen -= 15
        print("Ha habido una fuga de oxígeno.")
    elif event == 2:
        energy += 10
        print("Los paneles solares han cargado energía.")
    elif event == 3:
        food += 15
        print("Has encontrado suministros extra.")
    else:
        print("No ha ocurrido ningún incidente.")

    oxygen -= 10
    food -= 10
    energy -= 5
    print("Consumo diario aplicado.")

    if oxygen <= 0 or food <= 0 or energy <= 0:
        print("No has sobrevivido. La nave se ha quedado sin recursos.")
        break

if day == 7 and oxygen > 0 and food > 0 and energy > 0:
    print("¡Has sobrevivido hasta la llegada del rescate!")
