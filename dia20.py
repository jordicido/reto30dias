num_canciones = int(input("¿Cuántas canciones quieres añadir?: "))
playlist = []

for i in range(1, num_canciones + 1):
    cancion = input(f"Canción {i}: ")
    playlist.append(cancion)

print("\n----- PLAYLIST -----\n")
for i in range(num_canciones):
    print(f"{i + 1}. {playlist[i]}")

while True:
    consulta = input("\n¿Qué quieres consultar? (posición/nombre/salir): ").strip().lower()
    
    if consulta == "salir":
        print("¡Hasta luego!")
        break
    elif consulta == "posición":
        try:
            pos = int(input("¿Qué posición quieres consultar? "))
            if 1 <= pos <= num_canciones:
                print(f"La canción en la posición {pos} es: {playlist[pos - 1]}")
            else:
                print("Posición fuera de rango.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")
    elif consulta == "nombre":
        nombre = input("¿Qué canción quieres buscar? ")
        if nombre in playlist:
            print(f"La canción existe en la playlist.\nPosición: {playlist.index(nombre) + 1}")
        else:
            print("Canción no encontrada.")
    else:
        print("Opción no válida. Por favor, elige 'posición', 'nombre' o 'salir'.")