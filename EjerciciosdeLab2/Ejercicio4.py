def transformar_lista(lista, opcion):
    nueva_lista = []

    for palabra in lista:
        if opcion == 1:
            nueva_lista.append(palabra.upper())
        elif opcion == 2:
            nueva_lista.append(palabra.lower())
        elif opcion == 3:
            nueva_lista.append(palabra.capitalize())

    return nueva_lista


texto = input("Ingrese palabras separadas por espacio: ")
lista = texto.split()

opcion = int(input("Ingrese opción (1, 2 o 3): "))

resultado = transformar_lista(lista, opcion)
print("Resultado:", resultado)
