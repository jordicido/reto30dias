import random

def crear_personaje():
    nombre = input("Nombre del personaje: ")
    vida = int(input("Vida: "))
    ataque = int(input("Ataque: "))
    defensa = int(input("Defensa: "))
    poder = vida + ataque + defensa

    personaje = {
        "nombre": nombre,
        "vida": vida,
        "ataque": ataque,
        "defensa": defensa,
        "poder": poder,
        "victorias": 0
    }
    personajes.append(personaje)
    print("Personaje creado correctamente.")

def ver_personajes():
    if not personajes:
        print("No hay personajes creados.")
        return

    print("----- PERSONAJES -----")
    for i, personaje in enumerate(personajes, 1):
        print(f"{i}. {personaje['nombre']}")
        print(f"   Vida: {personaje['vida']}")
        print(f"   Ataque: {personaje['ataque']}")
        print(f"   Defensa: {personaje['defensa']}")
        print(f"   Poder: {personaje['poder']}")

def combatir():
    nombre_atacante = input("Nombre del atacante: ")
    nombre_defensor = input("Nombre del defensor: ")

    atacante = None
    defensor = None

    for personaje in personajes:
        if personaje["nombre"].lower() == nombre_atacante.lower():
            atacante = personaje
        if personaje["nombre"].lower() == nombre_defensor.lower():
            defensor = personaje

    if not atacante or not defensor:
        print("Uno o ambos personajes no existen.")
        return

    if atacante["nombre"].lower() == defensor["nombre"].lower():
        print("Un personaje no puede atacarse a sí mismo.")
        return

    daño = max(atacante["ataque"] - defensor["defensa"] + random.randint(-5, 5), 1)
    defensor["vida"] -= daño

    print(f"{atacante['nombre']} ataca a {defensor['nombre']}.")
    print(f"Daño realizado: {daño}")

    if defensor["vida"] <= 0:
        print(f"¡{defensor['nombre']} ha sido derrotado!")
        personajes.remove(defensor)
        atacante["victorias"] += 1

def ver_clasificacion():
    if not personajes:
        print("No hay personajes vivos.")
        return

    personaje_mas_vida = max(personajes, key=lambda p: p["vida"])
    personaje_menos_vida = min(personajes, key=lambda p: p["vida"])

    print("----- CLASIFICACIÓN -----")
    print(f"Personajes vivos: {len(personajes)}")
    print(f"Personaje con más vida: {personaje_mas_vida['nombre']} ({personaje_mas_vida['vida']} PV)")
    print(f"Personaje con menos vida: {personaje_menos_vida['nombre']} ({personaje_menos_vida['vida']} PV)")
    print("----- VICTORIAS -----")
    for personaje in sorted(personajes, key=lambda p: p["victorias"], reverse=True):
        print(f"{personaje['nombre']}: {personaje['victorias']} victorias")

personajes = []

while True:
    print("----- CREADOR DE PERSONAJES -----")
    print("1. Crear personaje")
    print("2. Ver personajes")
    print("3. Combatir")
    print("4. Ver clasificación")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        crear_personaje()
    elif opcion == "2":
        ver_personajes()
    elif opcion == "3":
        combatir()
    elif opcion == "4":
        ver_clasificacion()
    elif opcion == "5":
        print("Fin de la Arena de Combate.")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")