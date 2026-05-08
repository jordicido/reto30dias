student_name = input("Ingrese el nombre del alumno: ")
grade = float(input("Ingrese la nota (0 a 10): "))

if grade < 0 or grade > 10:
    print("Nota no válida")
else:
    if grade < 5:
        result = "Suspenso"
        message = "Hay que seguir trabajando"
    elif grade < 7:
        result = "Aprobado"
        message = "Buen trabajo"
    elif grade < 9:
        result = "Notable"
        message = "Buen trabajo"
    else:
        result = "Sobresaliente"
        message = "Buen trabajo"

    print(f"Alumno: {student_name}")
    print(f"Nota: {grade}")
    print(f"Resultado: {result}")
    print(message)