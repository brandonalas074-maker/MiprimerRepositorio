def transformar_texto(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()


texto = input("Ingresa un texto: ")
opcion = int(input("Ingresa opción (1,2,3): "))

print(transformar_texto(texto, opcion))
