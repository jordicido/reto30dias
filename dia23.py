def mostrar_inventario(inventario):
    print("----- INVENTARIO DEL MERCADER -----")
    for producto, cantidad in inventario.items():
        print(f"{producto} → {cantidad} unidades")
    total_unidades = sum(inventario.values())
    print(f"Total de unidades: {total_unidades}")

def consultar_producto(inventario):
    producto = input("Producto: ")
    if producto in inventario:
        print(f"{producto}: {inventario[producto]} unidades")
    else:
        print("Ese producto no existe en el inventario.")

def añadir_unidades(inventario):
    producto = input("Producto: ")
    try:
        cantidad_a_añadir = int(input("Cantidad a añadir: "))
        if cantidad_a_añadir <= 0:
            print("La cantidad debe ser mayor que 0.")
            return
    except ValueError:
        print("Cantidad no válida.")
        return

    if producto in inventario:
        print(f"{producto} tenía {inventario[producto]} unidades.")
        inventario[producto] += cantidad_a_añadir
        print(f"Ahora tiene {inventario[producto]} unidades.")
    else:
        inventario[producto] = cantidad_a_añadir
        print("Producto nuevo añadido al inventario.")

def vender_producto(inventario):
    producto = input("Producto: ")
    if producto not in inventario:
        print("Ese producto no existe.")
        return

    try:
        cantidad_a_vender = int(input("Cantidad a vender: "))
        if cantidad_a_vender <= 0:
            print("La cantidad debe ser mayor que 0.")
            return
    except ValueError:
        print("Cantidad no válida.")
        return

    if inventario[producto] < cantidad_a_vender:
        print("No hay suficientes unidades.")
    else:
        inventario[producto] -= cantidad_a_vender
        print("Venta realizada correctamente.")
        if inventario[producto] == 0:
            del inventario[producto]

inventario = {
    "pocion": 3,
    "espada": 1,
    "escudo": 2
}

while True:
    print("\n----- INVENTARIO DEL MERCADER -----")
    print("1. Ver inventario")
    print("2. Consultar producto")
    print("3. Añadir unidades")
    print("4. Vender producto")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        mostrar_inventario(inventario)
    elif opcion == "2":
        consultar_producto(inventario)
    elif opcion == "3":
        añadir_unidades(inventario)
    elif opcion == "4":
        vender_producto(inventario)
    elif opcion == "5":
        print("Inventario cerrado.")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")