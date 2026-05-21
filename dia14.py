rows = int(input("Número de filas: "))
columns = int(input("Número de columnas: "))
initial_value = int(input("¿Las coordenadas empiezan desde 1 o desde 0? (1/0): "))

for i in range(initial_value, rows + initial_value):
    for j in range(initial_value, columns + initial_value):
        print(f"({i},{j})", end=" ")
    print()

row_special = int(input("Fila especial: "))
column_special = int(input("Columna especial: "))

for i in range(initial_value, rows + initial_value):
    for j in range(initial_value, columns + initial_value):
        if i == row_special and j == column_special:
            print("  X  ", end=" ")
        else:
            print(f"({i},{j})", end=" ")
    print()
