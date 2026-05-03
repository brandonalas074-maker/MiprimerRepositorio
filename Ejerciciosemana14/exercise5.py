def positivos(lista):
    resultado = []
    for num in lista:
        if num > 0:
            resultado.append(num)
    return resultado


print(positivos([-3, 5, -1, 8, 0]))
