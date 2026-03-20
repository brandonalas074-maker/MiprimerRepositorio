# Solicitaremos una frase al usuario
frase = input("Ingresa una frase: ")

# Eliminamos los espacios
frasesinespacios = frase.replace(" ", "")

# Contaremos los caracteres sin espacios
cantidad = len(frasesinespacios)

# Mostraremos el resultado
print("Cantidad de letras (sin espacios):", cantidad)
