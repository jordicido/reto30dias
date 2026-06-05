import random

cartas = [
    "Caballero",
    "Arquera",
    "Mago",
    "Gigante",
    "Dragón",
    "Bruja",
    "Príncipe"
]
rarezas = {
    "Caballero": "Común",
    "Arquera": "Común",
    "Mago": "Especial",
    "Gigante": "Especial",
    "Bruja": "Épica",
    "Príncipe": "Épica",
    "Dragón": "Legendaria"
}
coleccion = {carta: 0 for carta in cartas}

while True:
    print("\n----- APERTURA DE SOBRES -----\n")
    print("1. Abrir sobre")
    print("2. Ver colección")
    print("3. Consultar carta")
    print("4. Ver estadísticas")
    print("5. Intercambiar cartas")
    print("6. Salir")

    opcion = input("\nElige una opción: ")

    if opcion == "1":
        nuevas_cartas = random.choices(cartas, k=5)
        print("\nHas obtenido:\n")
        for carta in nuevas_cartas:
            print(carta)
            coleccion[carta] += 1

        if all(cantidad > 0 for cantidad in coleccion.values()):
            print("\n¡COLECCIÓN COMPLETADA!\n")
            print("Has conseguido las 7 cartas del juego.")

    elif opcion == "2":
        print("\nTu colección:\n")
        for carta, cantidad in coleccion.items():
            print(f"{carta} → {cantidad} ({rarezas[carta]})")

    elif opcion == "3":
        carta_consulta = input("\n¿Qué carta quieres consultar? ")
        if carta_consulta in coleccion:
            cantidad = coleccion[carta_consulta]
            if cantidad > 0:
                print(f"\nTienes {cantidad} {carta_consulta}(s).")
            else:
                print("\nNo has conseguido esa carta todavía.")
        else:
            print("\nEsa carta no existe.")

    elif opcion == "4":
        cartas_diferentes = sum(1 for cantidad in coleccion.values() if cantidad > 0)
        carta_mas_obtenida = max(coleccion, key=coleccion.get)
        carta_menos_obtenida = min(coleccion, key=coleccion.get)
        total_cartas = sum(coleccion.values())

        print(f"\nCartas diferentes: {cartas_diferentes}")
        print(f"\nCarta más obtenida:\n{carta_mas_obtenida} ({coleccion[carta_mas_obtenida]})")
        print(f"\nCarta menos obtenida:\n{carta_menos_obtenida} ({coleccion[carta_menos_obtenida]})")
        print(f"\nTotal de cartas:\n{total_cartas}")

    elif opcion == "5":
        carta_intercambio = input("\n¿Qué carta quieres intercambiar? ")
        if carta_intercambio in coleccion and coleccion[carta_intercambio] >= 5:
            coleccion[carta_intercambio] -= 5
            nueva_carta = random.choice(cartas)
            coleccion[nueva_carta] += 1
            print(f"\nHas intercambiado 5 {carta_intercambio}(s) por 1 {nueva_carta}.")
        else:
            print("\nNo tienes suficientes copias de esa carta para intercambiar.")

    elif opcion == "6":
        print("\n¡Hasta luego!")
        break

    else:
        print("\nOpción no válida. Por favor, elige una opción del menú.")