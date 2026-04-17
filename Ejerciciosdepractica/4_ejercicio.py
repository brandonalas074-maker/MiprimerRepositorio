while True:
    numero = int(input("Ingresa un número: "))

    if numero != 0:
        break
    else:
        print("No ingreses el numero cero")

if numero % 2 == 0:
    print("Par")
else:
    print("Impar")
