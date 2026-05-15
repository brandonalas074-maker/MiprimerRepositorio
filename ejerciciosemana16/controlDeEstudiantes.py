# Sistema de control de estudiantes

# Arrays (listas)
nombres = []
notas = []

while True:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Mostrar promedio general")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    # match-case para controlar el menú
    match opcion:

        case "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            nota = float(input("Ingrese la nota del estudiante: "))

            nombres.append(nombre)
            notas.append(nota)

            # if y elif para clasificar
            if nota >= 9:
                estado = "Excelente"
            elif nota >= 7:
                estado = "Aprobado"
            elif nota >= 6:
                estado = "Regular"
            else:
                estado = "Reprobado"

            print(f"Estudiante agregado correctamente. Estado: {estado}")

        case "2":
            if len(nombres) == 0:
                print("No hay estudiantes registrados.")
            else:
                print("\n===== LISTA DE ESTUDIANTES =====")

                # for para recorrer listas
                for i in range(len(nombres)):

                    if notas[i] >= 9:
                        estado = "Excelente"
                    elif notas[i] >= 7:
                        estado = "Aprobado"
                    elif notas[i] >= 6:
                        estado = "Regular"
                    else:
                        estado = "Reprobado"

                    print(f"Nombre: {nombres[i]} | Nota: {notas[i]} | Estado: {estado}")

        case "3":
            buscar = input("Ingrese el nombre del estudiante a buscar: ")

            encontrado = False

            for i in range(len(nombres)):
                if nombres[i].lower() == buscar.lower():

                    if notas[i] >= 9:
                        estado = "Excelente"
                    elif notas[i] >= 7:
                        estado = "Aprobado"
                    elif notas[i] >= 6:
                        estado = "Regular"
                    else:
                        estado = "Reprobado"

                    print(f"Estudiante encontrado:")
                    print(f"Nombre: {nombres[i]}")
                    print(f"Nota: {notas[i]}")
                    print(f"Estado: {estado}")

                    encontrado = True
                    break

            if not encontrado:
                print("Estudiante no encontrado.")

        case "4":
            if len(notas) == 0:
                print("No hay notas registradas.")
            else:
                suma = 0

                for nota in notas:
                    suma += nota

                promedio = suma / len(notas)

                print(f"El promedio general es: {promedio:.2f}")

        case "5":
            print("Saliendo del programa...")
            break

        case _:
            print("Opción inválida. Intente nuevamente.")
