password = "python2026"
attempts = 0

while True:
    user_input = input("Introduce la contraseña: ")
    attempts += 1

    if user_input == password:
        print("Acceso concedido.\nBienvenido al sistema.")
        print(f"Has necesitado {attempts} intentos.")
        break
    else:
        if attempts == 1:
            print("Contraseña incorrecta. Inténtalo de nuevo.")
        elif attempts == 2:
            print("Contraseña incorrecta. Último intento.")
        elif attempts == 3:
            print("Cuenta bloqueada.")
            break

    