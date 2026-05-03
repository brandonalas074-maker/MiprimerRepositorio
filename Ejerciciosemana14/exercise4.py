def numero_mayor(lista):
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor


numeros = []
for i in range(8):
    numeros.append(int(input("Ingrese un número: ")))

print(numero_mayor(numeros))
