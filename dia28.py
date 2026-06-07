import random

def crear_personaje():
    nombre = input("Nombre: ")
    vida = int(input("Vida: "))
    ataque = int(input("Ataque: "))
    defensa = int(input("Defensa: "))

    personaje = {
        "nombre": nombre,
        "vida": vida,
        "ataque": ataque,
        "defensa": defensa,
        "monedas": 50,
        "victorias": 0,
        "inventario": []
    }

    personajes.append(personaje)
    print(f"Personaje {nombre} creado con éxito.")

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
        print(f"   Monedas: {personaje['monedas']}")
        print(f"   Inventario: {', '.join(personaje['inventario'])}")

def ver_tienda():
    print("----- TIENDA DE EQUIPAMIENTO -----")
    for i, objeto in enumerate(tienda, 1):
        print(f"{i}. {objeto['nombre']}")
        print(f"   Precio: {objeto['precio']}")
        print(f"   Ataque: +{objeto['ataque']}")
        print(f"   Defensa: +{objeto['defensa']}")
        print(f"   Vida: +{objeto['vida']}")

def comprar_objeto():
    nombre_personaje = input("Nombre del personaje: ")
    numero_objeto = int(input("Número del objeto: ")) - 1

    personaje = next((p for p in personajes if p["nombre"].lower() == nombre_personaje.lower()), None)

    if not personaje:
        print("Personaje no encontrado.")
        return

    if numero_objeto < 0 or numero_objeto >= len(tienda):
        print("Objeto no encontrado.")
        return

    objeto = tienda[numero_objeto]

    if personaje["monedas"] < objeto["precio"]:
        print("No tienes monedas suficientes.")
        return

    if objeto["nombre"] in personaje["inventario"]:
        print("Ya has comprado este objeto.")
        return

    personaje["monedas"] -= objeto["precio"]
    personaje["ataque"] += objeto["ataque"]
    personaje["defensa"] += objeto["defensa"]
    personaje["vida"] += objeto["vida"]
    personaje["inventario"].append(objeto["nombre"])

    print(f"{personaje['nombre']} ha comprado {objeto['nombre']}.")
    print(f"Ataque: {personaje['ataque']}")
    print(f"Defensa: {personaje['defensa']}")
    print(f"Vida: {personaje['vida']}")
    print(f"Monedas: {personaje['monedas']}")

personajes = []
tienda = [
    {"nombre": "Espada de hierro", "precio": 30, "ataque": 10, "defensa": 0, "vida": 0},
    {"nombre": "Escudo de madera", "precio": 25, "ataque": 0, "defensa": 8, "vida": 0},
    {"nombre": "Poción vital", "precio": 20, "ataque": 0, "defensa": 0, "vida": 20},
    {"nombre": "Armadura ligera", "precio": 40, "ataque": 0, "defensa": 12, "vida": 10}
]

while True:
    print("\n----- TIENDA DE EQUIPAMIENTO -----")
    print("1. Crear personaje")
    print("2. Ver personajes")
    print("3. Ver tienda")
    print("4. Comprar objeto")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        crear_personaje()
    elif opcion == "2":
        ver_personajes()
    elif opcion == "3":
        ver_tienda()
    elif opcion == "4":
        comprar_objeto()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")