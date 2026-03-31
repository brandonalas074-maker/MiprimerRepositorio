def transformar_contar(texto, opcion):
    if opcion == 1:
        resultado = texto.upper()
    elif opcion == 2:
        resultado = texto.lower()
    elif opcion == 3:
        resultado = texto.capitalize()
    else:
        return "Opción inválida"

    return len(resultado)


texto = input("Ingrese un texto: ")
opcion = int(input("Ingrese opción: "))

print("Cantidad de caracteres:", transformar_contar(texto, opcion))
