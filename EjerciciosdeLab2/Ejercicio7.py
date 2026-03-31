def transformaciones_multiples(texto, opciones):
    for opcion in opciones:
        if opcion == 1:
            texto = texto.upper()
        elif opcion == 2:
            texto = texto.lower()
        elif opcion == 3:
            texto = texto.capitalize()
    return texto


texto = input("Ingrese un texto: ")

opciones = input("Ingrese opciones separadas por espacio (ej: 1 2 3): ")
lista_opciones = [int(x) for x in opciones.split()]

resultado = transformaciones_multiples(texto, lista_opciones)

print("Resultado final:", resultado)
