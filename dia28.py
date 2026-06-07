'''
# DÍA 28 — “Tienda de equipamiento”

## Objetivo

Continuar con el proyecto de personajes trabajando listas de diccionarios, modificación de estadísticas e inventario.

---

## Continuación de los retos anteriores

En el **Día 26** creaste personajes con vida, ataque y defensa.

En el **Día 27** esos personajes pudieron combatir en la arena.

Ahora los personajes podrán comprar equipamiento para mejorar sus estadísticas antes de volver al combate.

---

## Enunciado

Crea un programa que simule una tienda de equipamiento para los personajes.

Cada personaje seguirá teniendo esta estructura:

```python
{
    "nombre": "Aria",
    "vida": 100,
    "ataque": 25,
    "defensa": 10,
    "monedas": 50
}
```

Todos los personajes estarán guardados en una lista:

```python
personajes = []
```

---

## Tienda inicial

La tienda tendrá varios objetos disponibles.

Cada objeto será un diccionario:

```python
{
    "nombre": "Espada de hierro",
    "precio": 30,
    "ataque": 10,
    "defensa": 0,
    "vida": 0
}
```

La tienda será una lista de diccionarios:

```python
tienda = [
    {"nombre": "Espada de hierro", "precio": 30, "ataque": 10, "defensa": 0, "vida": 0},
    {"nombre": "Escudo de madera", "precio": 25, "ataque": 0, "defensa": 8, "vida": 0},
    {"nombre": "Poción vital", "precio": 20, "ataque": 0, "defensa": 0, "vida": 20},
    {"nombre": "Armadura ligera", "precio": 40, "ataque": 0, "defensa": 12, "vida": 10}
]
```

---

## Menú principal

```text
----- TIENDA DE EQUIPAMIENTO -----

1. Crear personaje
2. Ver personajes
3. Ver tienda
4. Comprar objeto
5. Salir
```

---

## Opción 1 — Crear personaje

Pedir:

```text
Nombre:
Vida:
Ataque:
Defensa:
```

El personaje empezará con:

```text
50 monedas
```

---

## Opción 2 — Ver personajes

Mostrar todos los personajes con sus estadísticas:

```text
Aria
Vida: 100
Ataque: 25
Defensa: 10
Monedas: 50
```

---

## Opción 3 — Ver tienda

Mostrar todos los objetos disponibles:

```text
1. Espada de hierro
   Precio: 30
   Ataque: +10
   Defensa: +0
   Vida: +0

2. Escudo de madera
   Precio: 25
   Ataque: +0
   Defensa: +8
   Vida: +0
```

---

## Opción 4 — Comprar objeto

El programa debe pedir:

```text
Nombre del personaje:
Número del objeto:
```

Después debe comprobar:

* Que el personaje existe.
* Que el objeto existe.
* Que el personaje tiene monedas suficientes.

Si todo es correcto:

1. Restar el precio a las monedas del personaje.
2. Sumar las mejoras del objeto a sus estadísticas.
3. Mostrar el resultado.

Ejemplo:

```text
Aria ha comprado Espada de hierro.

Ataque: 25 → 35
Monedas: 50 → 20
```

Si no tiene monedas suficientes:

```text
No tienes monedas suficientes.
```

---

## Requisitos

* Usar listas de diccionarios.
* Buscar personajes por nombre.
* Acceder a objetos por posición.
* Modificar valores dentro del diccionario del personaje.
* Validar personajes inexistentes.
* Validar objetos inexistentes.
* Validar monedas suficientes.
* Mantener el menú activo hasta salir.

---

## Ampliación

### Nivel 1 — Inventario del personaje

Añadir a cada personaje una lista de objetos comprados:

```python
"inventario": []
```

Cuando compre un objeto, añadir su nombre al inventario.

---

### Nivel 2 — Evitar compras repetidas

Un personaje no puede comprar dos veces el mismo objeto.

'''

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