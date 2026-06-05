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
        "poder": poder
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
def buscar_personaje():
    nombre = input("Nombre del personaje a buscar: ")
    for personaje in personajes:
        if personaje["nombre"].lower() == nombre.lower():
            print(f"Nombre: {personaje['nombre']}")
            print(f"Vida: {personaje['vida']}")
            print(f"Ataque: {personaje['ataque']}")
            print(f"Defensa: {personaje['defensa']}")
            print(f"Poder: {personaje['poder']}")
            return
    print("Personaje no encontrado.")

def buscar_personaje_mas_fuerte():
    if not personajes:
        print("No hay personajes creados.")
        return

    personaje_mas_fuerte = {}

    for personaje in personajes:
        if not personaje_mas_fuerte or personaje["poder"] > personaje_mas_fuerte["poder"]:
            personaje_mas_fuerte = personaje
    
    print(f"Personaje más fuerte: {personaje_mas_fuerte['nombre']}")
    print(f"Poder: {personaje_mas_fuerte['poder']}")

def eliminar_personaje():
    nombre = input("Nombre del personaje a eliminar: ")
    for i, personaje in enumerate(personajes):
        if personaje["nombre"].lower() == nombre.lower():
            del personajes[i]
            print("Personaje eliminado.")
            return
    print("Personaje no encontrado.")

personajes = []

while True:
    print("----- CREADOR DE PERSONAJES -----")
    print("1. Crear personaje")
    print("2. Ver personajes")
    print("3. Buscar personaje más fuerte")
    print("4. Buscar personaje")
    print("5. Eliminar personaje")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        crear_personaje()
    elif opcion == "2":
        ver_personajes()
    elif opcion == "3":
        buscar_personaje_mas_fuerte()
    elif opcion == "4":
        buscar_personaje()
    elif opcion == "5":
        eliminar_personaje()
    elif opcion == "6":
        print("Fin del creador de personajes.")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")