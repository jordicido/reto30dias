pruebas = [
    {
        "nombre": "Puerta antigua",
        "pregunta": "¿Cuánto es 7 x 8?",
        "respuesta": "56",
        "puntos": 10,
        "resuelta": False,
        "intentos": 0
    },
    {
        "nombre": "Caja fuerte",
        "pregunta": "¿Qué lenguaje estamos aprendiendo?",
        "respuesta": "python",
        "puntos": 15,
        "resuelta": False,
        "intentos": 0
    },
    {
        "nombre": "Panel secreto",
        "pregunta": "¿Cuántos días tiene una semana?",
        "respuesta": "7",
        "puntos": 10,
        "resuelta": False,
        "intentos": 0
    }
]

while True:
    print("----- ESCAPE ROOM DIGITAL -----")
    print("1. Ver pruebas")
    print("2. Resolver prueba")
    print("3. Ver puntuación")
    print("4. Ver progreso")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        for i, prueba in enumerate(pruebas, 1):
            estado = "Resuelta" if prueba["resuelta"] else "Pendiente"
            print(f"{i}. {prueba['nombre']} → {estado}")
    elif opcion == "2":
        for i, prueba in enumerate(pruebas, 1):
            estado = "Resuelta" if prueba["resuelta"] else "Pendiente"
            print(f"{i}. {prueba['nombre']} → {estado}")
        eleccion = int(input("Elige una prueba: ")) - 1
        if eleccion < 0 or eleccion >= len(pruebas):
            print("Opción no válida.")
            continue
        prueba_elegida = pruebas[eleccion]
        if prueba_elegida["resuelta"]:
            print("Esa prueba ya estaba resuelta.")
            continue
        respuesta_usuario = input(prueba_elegida["pregunta"] + " ")
        if respuesta_usuario.lower() == prueba_elegida["respuesta"].lower():
            print("Respuesta correcta.")
            print(f"Has ganado {prueba_elegida['puntos']} puntos.")
            prueba_elegida["resuelta"] = True
            if all(prueba["resuelta"] for prueba in pruebas):
                puntuacion_final = sum(prueba["puntos"] for prueba in pruebas)
                print("¡Has escapado del escape room!")
                print(f"Puntuación final: {puntuacion_final} puntos")
                break
        else:
            print("Respuesta incorrecta.")
            prueba_elegida["intentos"] += 1
            # Penalización de 2 puntos por fallo
            prueba_elegida["puntos"] = max(prueba_elegida["puntos"] - 2, 0)
    elif opcion == "3":
        puntuacion_total = sum(prueba["puntos"] for prueba in pruebas if prueba["resuelta"])
        print(f"Puntuación actual: {puntuacion_total} puntos")
    elif opcion == "4":
        resueltas = sum(1 for prueba in pruebas if prueba["resuelta"])
        pendientes = len(pruebas) - resueltas
        print(f"Pruebas resueltas: {resueltas}/{len(pruebas)}")
        print(f"Pruebas pendientes: {pendientes}")
        if resueltas == len(pruebas):
            puntuacion_final = sum(prueba["puntos"] for prueba in pruebas)
            print("¡Has escapado del escape room!")
            print(f"Puntuación final: {puntuacion_final} puntos")
            break
    elif opcion == "5":
        print("Has abandonado el escape room.")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
