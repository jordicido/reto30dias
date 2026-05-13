total = 0
products = []
expensive_product = None

while True:
    print("\n----- SUPERMERCADO -----")
    print("1. Añadir producto")
    print("2. Ver total actual")
    print("3. Aplicar descuento")
    print("4. Finalizar compra")
    print("5. Vaciar carrito")

    choice = input("Selecciona una opción: ")

    if choice == "1":
        name = input("Nombre del producto: ")
        price = float(input("Precio del producto: "))

        if price < 0:
            print("El precio no puede ser negativo.")
            continue

        total += price
        products.append((name, price))

        if expensive_product is None or price > expensive_product[1]:
            expensive_product = (name, price)

        print(f"Producto '{name}' añadido correctamente. Total actual: {total:.2f}€")

    elif choice == "2":
        print(f"Total actual: {total:.2f}€")

    elif choice == "3":
        if total > 100:
            discount = total * 0.20
            print(f"Descuento aplicado: 20% ({discount:.2f}€)")
        elif total > 50:
            discount = total * 0.10
            print(f"Descuento aplicado: 10% ({discount:.2f}€)")
        else:
            discount = 0
            print("No hay descuento disponible.")

    elif choice == "4":
        if total > 100:
            discount = total * 0.20
        elif total > 50:
            discount = total * 0.10
        else:
            discount = 0

        final_price = total - discount
        print(f"Total antes del descuento: {total:.2f}€")
        print(f"Descuento aplicado: {discount:.2f}€")
        print(f"Precio final: {final_price:.2f}€")
        break

    elif choice == "5":
        total = 0
        products = []
        expensive_product = None
        print("Carrito vaciado.")

    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")