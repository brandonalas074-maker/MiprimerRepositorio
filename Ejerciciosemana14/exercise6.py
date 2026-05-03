import random


def mayores_50(lista):
    contador = 0
    for num in lista:
        if num > 50:
            contador += 1
    return contador


numeros = [random.randint(1, 100) for _ in range(10)]
print(numeros)
print("Mayores a 50:", mayores_50(numeros))
