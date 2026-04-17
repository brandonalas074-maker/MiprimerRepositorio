while True:
    edad = int(input("Ingresa tu edad: "))

    if edad >= 0:
        break
    else:
        print("Edad inválida")

if edad < 18:
    print("Menor de edad")
elif edad < 60:
    print("Mayor de edad")
else:
    print("Adulto mayor")
