product_name = input("Ingrese el nombre del producto: ")
unit_price = float(input("Ingrese el precio unitario: "))
quantity = int(input("Ingrese la cantidad: "))
subtotal = unit_price * quantity
iva = subtotal * 0.21
total = subtotal + iva

print("------ TICKET ------")
print(f"Producto: {product_name}")
print(f"Cantidad: {quantity}")
print(f"Precio unitario: {unit_price}€")
print(f"Subtotal: {subtotal}€")
print(f"IVA (21%): {iva}€")
print(f"TOTAL: {total:.2f}€")
print("-------------------")

if total < 20:
    print("Compra pequeña")
else:
    print("Compra grande")