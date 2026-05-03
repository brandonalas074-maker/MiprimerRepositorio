def nombres_largos(nombres):
    resultado = []
    for nombre in nombres:
        if len(nombre) > 5:
            resultado.append(nombre)
    return resultado


nombres = []
for i in range(10):
    nombres.append(input("Ingrese un nombre: "))

print(nombres_largos(nombres))
