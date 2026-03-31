def transformar_validar(texto, opcion):
    if opcion not in [1, 2, 3]:
        return "Opcion invalida"

    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    else:
        return texto.capitalize()


texto = input("Ingrese un texto: ")
opcion = int(input("Ingrese opción: "))

print(transformar_validar(texto, opcion))
