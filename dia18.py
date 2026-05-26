frase = input("Introduce una frase: ")
caracter = input("¿Qué carácter quieres utilizar para el marco? ")
altura_interior = int(input("Altura interior: "))
longitud = len(frase) + 4
print(caracter * longitud)

for i in range(altura_interior):
    if i == altura_interior // 2:
        print(f"{caracter} {frase} {caracter}")
    else:
        print(f"{caracter}{' ' * (longitud - 2)}{caracter}")

if altura_interior % 2 == 0:
    print(f"{caracter}{' ' * (longitud - 2)}{caracter}")
print(caracter * longitud)
