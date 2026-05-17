grades = []
approved = 0
failed = 0

while True:
    try:
        grade = float(input("Introduce una nota (-1 para terminar): "))
        if grade == -1:
            break
        elif 0 <= grade <= 10:
            grades.append(grade)
            if grade >= 5:
                approved += 1
            else:
                failed += 1
        else:
            print("Nota inválida. Debe estar entre 0 y 10.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número.")

if grades:
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    total = len(grades)

    print("\n----- RESULTADOS -----\n")
    print(f"Media: {average:.2f}")
    print(f"Nota más alta: {highest}")
    print(f"Nota más baja: {lowest}")
    print(f"Total de notas: {total}")
    print(f"Aprobados: {approved}")
    print(f"Suspensos: {failed}")

    if total > 0:
        percentage_approved = (approved / total) * 100
        print(f"Porcentaje de aprobados: {percentage_approved:.2f}%")

    if average >= 8:
        classification = "Grupo excelente"
    elif average >= 5:
        classification = "Grupo aceptable"
    else:
        classification = "Grupo mejorable"

    print(f"Clasificación final: {classification}")