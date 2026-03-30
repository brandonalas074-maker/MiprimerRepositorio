def transformar_palabra(palabra, opcion):
    if opcion == 1:
        print(palabra.upper())
    elif opcion == 2:
        print(palabra.lower())
    elif opcion == 3:
        print(palabra.capitalize())
    else:
        print("Opción inválida")


palabra = input("Ingrese una palabra: ")
opcion = int(input("Ingrese opción (1, 2 o 3): "))

transformar_palabra(palabra, opcion)
