'''
# DÍA 4 — “Analizador de números”

## Objetivo

Trabajar comparaciones, condicionales múltiples y lógica combinada.

---

## Enunciado

Crea un programa capaz de analizar dos números introducidos por el usuario.

El programa debe:

1. Pedir dos números enteros

2. Mostrar:

   * Cuál es mayor
   * Cuál es menor
   * O indicar si son iguales

3. Calcular y mostrar:

   * La diferencia entre ambos
   * La suma de los dos números

4. Analizar además:

   * Si cada número es positivo, negativo o cero
   * Si cada número es par o impar

5. Mostrar toda la información de manera ordenada.

---

## Ejemplo de ejecución

```text
Introduce el primer número: 8
Introduce el segundo número: -3

----- RESULTADOS -----

Número mayor: 8
Número menor: -3

Suma: 5
Diferencia: 11

Número 1:
- Positivo
- Par

Número 2:
- Negativo
- Impar

----------------------
```

---

## Requisitos adicionales

* Deben contemplarse todos los casos posibles
* No repetir lógica innecesaria
* La salida debe estar bien estructurada
* Usar correctamente operadores matemáticos y condicionales

---

## Ampliación (nivel avanzado)

Añadir:

* Comprobar que los números introducidos son enteros válidos
* Permitir introducir números decimales y analizar su parte entera y decimal por separado

'''
def analyze_number(num):
    if num > 0:
        sign = "Positivo"
    elif num < 0:
        sign = "Negativo"
    else:
        sign = "Cero"
    parity = "Par" if num % 2 == 0 else "Impar"
    return sign, parity


number1 = int(input("Introduce el primer número: "))
number2 = int(input("Introduce el segundo número: "))

print("\n----- RESULTADOS -----\n")
if number1 > number2:
    print(f"Número mayor: {number1}")
    print(f"Número menor: {number2}")
elif number1 < number2:
    print(f"Número mayor: {number2}")
    print(f"Número menor: {number1}")
else:
    print("Los números son iguales")

print(f"\nSuma: {number1 + number2}")
print(f"Diferencia: {abs(number1 - number2)}\n")

sign1, parity1 = analyze_number(number1)
sign2, parity2 = analyze_number(number2)

print(f"\nNúmero 1:")
print(f"- {sign1}")
print(f"- {parity1}")

print(f"\nNúmero 2:")
print(f"- {sign2}")
print(f"- {parity2}")