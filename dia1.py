
name = input("¿Cuál es tu nombre? ").capitalize()
birth_year = int(input("¿En qué año naciste? "))
current_year = 2026
city = input("¿En qué ciudad vives? ")
age = current_year - birth_year

print(f"""
----- FICHA DE USUARIO -----
Nombre: {name}
Ciudad: {city}
Edad: {age}
-----------------------------
""")

if age < 30:
    print("Eres joven")
else:    
    print("Eres adulto")