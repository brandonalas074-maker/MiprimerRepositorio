nombre_completo = input("Ingrese su nombre completo: ")

# Convertimos a lista
lista_nombres = nombre_completo.split()

# Invertimos la lista
lista_invertida = lista_nombres[::-1]

# Ussamos For anidado
for palabra in lista_invertida:

    for letra in palabra:
        print(letra, end=".")

    print(" ", end="")
