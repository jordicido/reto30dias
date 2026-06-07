import random

parque = {
    "dinero": 100,
    "visitantes": 20,
    "satisfaccion": 70,
    "dia": 1
}

atracciones_disponibles = [
    {"nombre": "Montaña rusa", "precio": 40, "ingresos": 20},
    {"nombre": "Casa del terror", "precio": 25, "ingresos": 12},
    {"nombre": "Noria", "precio": 30, "ingresos": 15}
]

atracciones_construidas = []

print("----- BIENVENIDO AL PARQUE DE ATRACCIONES -----")
print("Elige la dificultad inicial:")
print("1. Fácil")
print("2. Normal")
print("3. Difícil")

dificultad = input("Elige una opción: ")

if dificultad == "1":
    parque["dinero"] = 150
    parque["satisfaccion"] = 80
elif dificultad == "2":
    parque["dinero"] = 100
    parque["satisfaccion"] = 70
elif dificultad == "3":
    parque["dinero"] = 70
    parque["satisfaccion"] = 60

while True:
    print(f"----- DÍA {parque['dia']} -----")
    print(f"Dinero: {parque['dinero']}€")
    print(f"Visitantes: {parque['visitantes']}")
    print(f"Satisfacción: {parque['satisfaccion']}")

    print("1. Construir atracción")
    print("2. Mejorar satisfacción")
    print("3. Hacer publicidad")
    print("4. Pasar al siguiente día")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        for i, atraccion in enumerate(atracciones_disponibles, 1):
            print(f"{i}. {atraccion['nombre']} (Precio: {atraccion['precio']}€, Ingresos: {atraccion['ingresos']}€)")
        eleccion = int(input("Elige una atracción para construir: ")) - 1
        if eleccion < 0 or eleccion >= len(atracciones_disponibles):
            print("Opción no válida.")
            continue
        atraccion_elegida = atracciones_disponibles[eleccion]
        if atraccion_elegida in atracciones_construidas:
            print("Ya has construido esta atracción.")
            continue
        if parque["dinero"] >= atraccion_elegida["precio"]:
            parque["dinero"] -= atraccion_elegida["precio"]
            atracciones_construidas.append(atraccion_elegida)
            print(f"Has construido la {atraccion_elegida['nombre']}.")
        else:
            print("No tienes dinero suficiente.")
    elif opcion == "2":
        if parque["dinero"] >= 30:
            parque["dinero"] -= 30
            parque["satisfaccion"] = min(parque["satisfaccion"] + 20, 100)
            print("Has mejorado la satisfacción de los visitantes.")
        else:
            print("No tienes dinero suficiente.")
    elif opcion == "3":
        if parque["dinero"] >= 20:
            parque["dinero"] -= 20
            parque["visitantes"] += 10
            print("Has hecho publicidad y atraído más visitantes.")
        else:
            print("No tienes dinero suficiente.")
    elif opcion == "4":
        ingresos = sum(atraccion["ingresos"] for atraccion in atracciones_construidas) + parque["visitantes"]
        parque["dinero"] += ingresos
        evento = random.randint(1, 4)
        if evento == 1:
            parque["visitantes"] = max(parque["visitantes"] - 5, 0)
            print("Ha llovido y algunos visitantes se han ido.")
        elif evento == 2:
            parque["visitantes"] += 15
            print("Un influencer ha recomendado el parque y han llegado más visitantes.")
        elif evento == 3:
            parque["satisfaccion"] = max(parque["satisfaccion"] - 15, 0)
            print("Ha habido una avería en una atracción y la satisfacción ha bajado.")
        else:
            print("Ha sido un día tranquilo sin eventos.")
        parque["satisfaccion"] = max(parque["satisfaccion"] - 5, 0)
        parque["dia"] += 1
        if parque["satisfaccion"] <= 0:
            print("El parque ha cerrado por malas reseñas.")
            break
        if parque["dia"] > 7:
            print("Fin de la semana.")
            print(f"Dinero final: {parque['dinero']}€")
            print(f"Atracciones construidas: {len(atracciones_construidas)}")
            print(f"Visitantes finales: {parque['visitantes']}")
            print(f"Satisfacción final: {parque['satisfaccion']}")
            break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
