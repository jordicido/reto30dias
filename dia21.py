import random

objetos_posibles = ["poción", "espada", "escudo", "llave", "moneda", "mapa", "antorcha", "llave dorada", "gema antigua", "pergamino mágico"]
mochila = []
objetos_especiales = set()
total_objetos_encontrados = 0

while True:
    print("----- MOCHILA DEL AVENTURERO -----")
    print("1. Encontrar objeto")
    print("2. Usar objeto")
    print("3. Ver mochila")
    print("4. Buscar objeto")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        objeto_encontrado = random.choice(objetos_posibles)
        print(f"Has encontrado: {objeto_encontrado}")
        if objeto_encontrado in ["llave dorada", "gema antigua", "pergamino mágico"]:
            objetos_especiales.add(objeto_encontrado)
            if len(objetos_especiales) == 3:
                print("¡Has completado la misión secreta!")
        total_objetos_encontrados += 1
        if len(mochila) >= 5:
            print("La mochila está llena. No puedes guardarlo.")
        elif objeto_encontrado in mochila:
            print("Ya tienes ese objeto en la mochila. No puedes guardarlo.")
        else:
            mochila.append(objeto_encontrado)
            print("Objeto añadido a la mochila.")
        print(f"Total objetos encontrados: {total_objetos_encontrados}")

    elif opcion == "2":
        objeto_a_usar = input("¿Qué objeto quieres usar? ")
        if objeto_a_usar in mochila:
            mochila.remove(objeto_a_usar)
            print(f"Has usado: {objeto_a_usar}")
        else:
            print("No tienes ese objeto en la mochila.")

    elif opcion == "3":
        if mochila:
            print("----- MOCHILA -----")
            for i, objeto in enumerate(mochila, start=1):
                print(f"{i}. {objeto}")
        else:
            print("La mochila está vacía.")

    elif opcion == "4":
        objeto_a_buscar = input("¿Qué objeto quieres buscar? ")
        if objeto_a_buscar in mochila:
            print("Sí tienes ese objeto.")
        else:
            print("No tienes ese objeto.")

    elif opcion == "5":
        print("Fin de la aventura.")
        break

    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")