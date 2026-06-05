mapas = ["Nuketown", "Raid", "Hijacked", "Standoff"]
votos = {mapa: 0 for mapa in mapas}

print("Mapas disponibles:")
for i, mapa in enumerate(mapas, 1):
    print(f"{i}. {mapa}")

num_jugadores = int(input("\n¿Cuántos jugadores van a votar?: "))
for i in range(1, num_jugadores + 1):
    while True:
        voto = int(input(f"Jugador {i}, elige mapa: "))
        if 1 <= voto <= len(mapas):
            votos[mapas[voto - 1]] += 1
            break
        else:
            print("Mapa no válido. Por favor, elige un mapa de la lista.")

max_votos = max(votos.values())
mapas_ganadores = [mapa for mapa, votos in votos.items() if votos == max_votos]
if len(mapas_ganadores) > 1:
    print(f"\nHay empate entre {', '.join(mapas_ganadores)}.")
    for i, mapa in enumerate(mapas_ganadores, 1):
        print(f"{i}. {mapa}")
    num_jugadores = int(input("\n¿Cuántos jugadores van a votar en la segunda ronda?: "))
    votos_segunda_ronda = {mapa: 0 for mapa in mapas_ganadores}
    for i in range(1, num_jugadores + 1):
        while True:
            voto = int(input(f"Jugador {i}, elige mapa: "))
            if 1 <= voto <= len(mapas_ganadores):
                votos_segunda_ronda[mapas_ganadores[voto - 1]] += 1
                break
            else:
                print("Mapa no válido. Por favor, elige un mapa de la lista.")
    max_votos_segunda_ronda = max(votos_segunda_ronda.values())
    mapas_ganadores_segunda_ronda = [mapa for mapa, votos in votos_segunda_ronda.items() if votos == max_votos_segunda_ronda]
    print(f"\nMapa elegido: {mapas_ganadores_segunda_ronda[0]}")
else:
    print(f"\nMapa elegido: {mapas_ganadores[0]}")