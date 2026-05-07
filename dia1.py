'''
Vas a crear un programa que genere una ficha de usuario en pantalla.

El programa debe:

Pedir al usuario:

- Nombre
- Año de nacimiento
- Ciudad
- Calcular la edad aproximada (suponiendo año actual 2026)

Mostrar la información con este formato:

```text
----- FICHA DE USUARIO -----
Nombre: Juan
Ciudad: Valencia
Edad aproximada: 20 años
---------------------------
```

## Requisitos adicionales

- El nombre debe mostrarse con la primera letra en mayúscula
- La edad debe ser un número (no texto)
- El formato debe respetar las líneas (estética mínima)

## Ampliación

Añadir una línea final:

- “Eres joven” si tiene menos de 30
- “Eres adulto” si tiene 30 o más
'''
name = input("¿Cuál es tu nombre? ").capitalize()
birth_year = int(input("¿En qué año naciste? "))
current_year = 2026
city = input("¿En qué ciudad vives? ")
age = current_year - birth_year

print(f"""
----- FICHA DE USUARIO -----
Nombre: {name}
Ciudad: {city}
Edad: {age}
-----------------------------
""")

if age < 30:
    print("Eres joven")
else:    
    print("Eres adulto")