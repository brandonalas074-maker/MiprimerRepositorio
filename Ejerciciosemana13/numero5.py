contraseña_correcta = "BEAT.28"
intentos = 0

while True:
    clave = input("Ingresa la contraseña: ")
    if clave == contraseña_correcta:
        print("Contraseña correcta.")
        break
    else:
        intentos += 1
        print("Contraseña incorrecta.")

for i in range(intentos):
    print(f"Intento fallido #{i+1}")
