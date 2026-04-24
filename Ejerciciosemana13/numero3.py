while True:
    n = int(input("Ingresa un número (-1 para salir): "))
    if n == -1:
        break
    for i in range(1, 11):
        resultado = n * i
        if resultado > 20:
            print(f"{n} x {i} = {resultado}")
