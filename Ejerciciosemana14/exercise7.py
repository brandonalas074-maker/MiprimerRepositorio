def mayores_edad(edades):
    contador = 0
    for edad in edades:
        if edad >= 18:
            contador += 1
    return contador


print(mayores_edad([15, 20, 17, 30, 18]))
