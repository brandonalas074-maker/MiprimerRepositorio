# Solicitaremos el correo electrónico al usuario
correo = input("Ingresa tu correo electrónico: ")

# Verificaremos si contiene el símbolo @
if "@" in correo:
    print("El correo parece válido")
else:
    print("El correo no es válido")
