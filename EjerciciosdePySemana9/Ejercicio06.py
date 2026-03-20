# 1. Solicitamos el nombre completo
nombre = input("Ingresa tu nombre completo: ")

# 2. Separamos en palabras
palabras = nombre.split()

# 3. Mostramos cada palabra en una linea diferente
for palabra in palabras:
    print(palabra)
