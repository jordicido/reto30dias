import random

def simulate_lap(car_name):
    time = random.randint(20, 40)
    print(f"{car_name} → {time} segundos")

    if time % 7 == 0:
        print("¡Derrape!")
        print("Penalización: +5 segundos")
        time += 5
        print(f"Tiempo final de la vuelta: {time} segundos")
    elif time % 11 == 0:
        print("¡Entrada en boxes!")
        print("Penalización: +10 segundos")
        time += 10
        print(f"Tiempo final de la vuelta: {time} segundos")

    return time

print("----- SIMULADOR DE CARRERA DE COCHES -----")
car1 = input("Nombre del coche 1: ")
car2 = input("Nombre del coche 2: ")

total_time_car1 = 0
total_time_car2 = 0
wins_car1 = 0
wins_car2 = 0
fastest_lap_time = float('inf')
fastest_lap_car = ""

for lap in range(1, 6):
    print(f"\n----- VUELTA {lap} -----")

    time_car1 = simulate_lap(car1)
    time_car2 = simulate_lap(car2)

    total_time_car1 += time_car1
    total_time_car2 += time_car2

    if time_car1 < time_car2:
        print(f"{car1} ha sido más rápido en esta vuelta.")
        wins_car1 += 1
    elif time_car2 < time_car1:
        print(f"{car2} ha sido más rápido en esta vuelta.")
        wins_car2 += 1
    else:
        print("¡Empate en esta vuelta!")
    
    if time_car1 < fastest_lap_time:
        fastest_lap_time = time_car1
        fastest_lap_car = car1
    if time_car2 < fastest_lap_time:
        fastest_lap_time = time_car2
        fastest_lap_car = car2

print(f"\n----- RESULTADO FINAL -----")
print(f"Tiempo total {car1}: {total_time_car1} segundos")
print(f"Tiempo total {car2}: {total_time_car2} segundos")

if total_time_car1 < total_time_car2:
    print(f"GANADOR: {car1}")
elif total_time_car2 < total_time_car1:
    print(f"GANADOR: {car2}")
else:
    print("¡Empate en la carrera!")

print(f"\n----- ESTADÍSTICAS -----")
print(f"{car1} ha ganado {wins_car1} vueltas.")
print(f"{car2} ha ganado {wins_car2} vueltas.")
print(f"Vuelta más rápida: {fastest_lap_time} segundos ({fastest_lap_car})")