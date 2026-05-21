import random

players = int(input("¿Cuántos jugadores participan? "))
matches = 0
victories = [0] * players

for i in range(players):
    for j in range(i + 1, players):
        matches += 1
        score_player_i = random.randint(0, 5)
        score_player_j = random.randint(0, 5)
        
        print(f"Jugador {i + 1} {score_player_i} - {score_player_j} Jugador {j + 1}")
        
        if score_player_i > score_player_j:
            victories[i] += 1
        elif score_player_j > score_player_i:
            victories[j] += 1

print(f"\nNúmero total de partidos jugados: {matches}")
print("Victorias por jugador:")
for i in range(len(victories)):
    print(f"Jugador {i + 1}: {victories[i]} victorias")