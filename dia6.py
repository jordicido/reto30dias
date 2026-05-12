'''
# DÍA 6 — “Simulador de contraseña”

## Objetivo

Introducir bucles mediante validación repetitiva de datos.

---

## Enunciado

Crea un programa que simule un sistema básico de acceso mediante contraseña.

El programa debe:

1. Tener una contraseña correcta guardada en una variable

2. Pedir al usuario que introduzca la contraseña

3. Si la contraseña es incorrecta:

   * Mostrar un mensaje de error
   * Volver a pedirla

4. El programa debe repetirse hasta que:

   * El usuario escriba la contraseña correcta

5. Cuando acierte:

   * Mostrar un mensaje de bienvenida

---

## Ejemplo de ejecución

```text
Introduce la contraseña: hola123

Contraseña incorrecta.

Introduce la contraseña: admin

Contraseña incorrecta.

Introduce la contraseña: python2026

Acceso concedido.
Bienvenido al sistema.
```

---

## Requisitos adicionales

* Debe utilizarse un bucle
* La contraseña correcta no puede cambiar durante la ejecución
* El programa debe seguir funcionando hasta acertar
* Los mensajes deben ser claros y ordenados

---

## Ampliación (nivel avanzado)

Añadir:

### Nivel 1

Contar cuántos intentos ha necesitado el usuario.

Ejemplo:

```text
Has necesitado 3 intentos.
```

---

### Nivel 2

Limitar el número máximo de intentos a 3.

Si falla 3 veces:

```text
Cuenta bloqueada.
```

---

### Nivel 3

Mostrar distintos mensajes según el número de intentos:

* Primer fallo → “Inténtalo de nuevo”
* Segundo fallo → “Último intento”
* Tercer fallo → “Acceso bloqueado”
'''

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

    