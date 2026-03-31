def transformar(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return "Opción inválida"


while True:
    print("\n--- MENÚ ---")
    print("1. Mayusculas")
    print("2. Minusculas")
    print("3. Capitalizar")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 4:
        print("Saliendo...")
        break

    if opcion not in [1, 2, 3]:
        print("Opción inválida")
        continue

    texto = input("Ingrese un texto: ")
    resultado = transformar(texto, opcion)
    print("Resultado:", resultado)
