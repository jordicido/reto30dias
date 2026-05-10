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