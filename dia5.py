# Definimos las cantidades de billetes y monedas en céntimos en una lista ordenada de mayor a menor
quantities = [50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
price = float(input("Precio de la compra: "))
money_given = float(input("Dinero entregado: "))

if money_given < price:
    print("Error: El dinero entregado es insuficiente.")
elif price < 0 or money_given < 0:
    print("Error: No se permiten cantidades negativas.")
else:
    change = int(money_given*100 - price*100)


    for quantity in quantities:
        if change >= quantity:
            count = change // quantity
            change %= quantity
            if quantity >= 500:
                print(f"Billetes de {quantity//100}€: {count}")
            else:
                print(f"Monedas de {quantity/100:.2f}€: {count}")