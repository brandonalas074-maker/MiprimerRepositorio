# Solicitaremos una frase a nuestro usuario
frase = input("Ingresa una frase: ")

# Verificar si termina con punto
if frase.endswith("."):
    print("La frase termina con un punto.")
else:
    print("La frase NO termina con un punto.")
