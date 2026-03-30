def transformar(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return "Opción inválida"


texto = input("Ingrese un texto: ")
opcion = int(input("Ingrese opción (1, 2, 3): "))

resultado = transformar(texto, opcion)
print("Resultado:", resultado)
