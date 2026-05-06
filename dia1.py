name = input("¿Cuál es tu nombre? ")
birth_year = int(input("¿En qué año naciste? "))
current_year = 2026
city = input("¿En qué ciudad vives? ")

print(f"""
----- FICHA DE USUARIO -----
Nombre: {name}
Ciudad: {city}
Edad: {current_year - birth_year}
-----------------------------
""")