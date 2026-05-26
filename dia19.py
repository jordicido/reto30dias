num_pilotos = int(input("¿Cuántos pilotos participan?: "))
puntos = []

for i in range(1, num_pilotos + 1):
    puntos_piloto = int(input(f"Puntos del piloto {i}: "))
    puntos.append(puntos_piloto)

print("\n----- CLASIFICACIÓN -----\n")
for i in range(num_pilotos):
    print(f"Piloto {i + 1} → {puntos[i]} puntos")

print(f"\nPuntuación máxima: {max(puntos)}")
print(f"Puntuación mínima: {min(puntos)}")
print(f"Media de puntos: {sum(puntos) / len(puntos):.2f}")

ganador_index = puntos.index(max(puntos))
print(f"\nPiloto ganador: Piloto {ganador_index + 1}")
print(f"Puntuación: {puntos[ganador_index]} puntos")