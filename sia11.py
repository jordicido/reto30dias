def draw_rectangle(rows, cols, char):
    for _ in range(rows):
        print(char * cols)

def draw_triangle_normal(height, char):
    for i in range(1, height + 1):
        print(char * i)

def draw_triangle_inverted(height, char):
    for i in range(height, 0, -1):
        print(char * i)

def draw_pyramid(height, char):
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        chars = char * (2 * i + 1)
        print(spaces + chars)

while True:
    print("\n----- GENERADOR DE PATRONES -----\n")
    print("1. Rectángulo")
    print("2. Triángulo normal")
    print("3. Triángulo invertido")
    print("4. Pirámide centrada")
    print("5. Salir")

    choice = input("\nElige una opción: ")

    if choice == '1':
        rows = int(input("Introduce el número de filas: "))
        cols = int(input("Introduce el número de columnas: "))
        char = input("¿Qué carácter quieres utilizar? ")
        draw_rectangle(rows, cols, char)
    elif choice == '2':
        height = int(input("Introduce la altura: "))
        char = input("¿Qué carácter quieres utilizar? ")
        draw_triangle_normal(height, char)
    elif choice == '3':
        height = int(input("Introduce la altura: "))
        char = input("¿Qué carácter quieres utilizar? ")
        draw_triangle_inverted(height, char)
    elif choice == '4':
        height = int(input("Introduce la altura: "))
        char = input("¿Qué carácter quieres utilizar? ")
        draw_pyramid(height, char)
    elif choice == '5':
        print("¡Gracias por usar el generador de patrones! ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 5.")

