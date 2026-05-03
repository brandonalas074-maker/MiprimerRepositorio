def suma_pares(lista):
    suma = 0
    for num in lista:
        if num % 2 == 0:
            suma += num
    return suma


print(suma_pares([1, 2, 3, 4, 6, 7, 10]))
