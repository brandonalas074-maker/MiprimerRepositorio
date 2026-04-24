positivos = 0
negativos = 0

while True:
    num = int(
        input("Ingresa un número, + O - (0 para ver visualizar resultado y salir): ")
    )
    if num == 0:
        break
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

for resultado in ["Positivos", "Negativos"]:
    if resultado == "Positivos":
        print("Cantidad de positivos:", positivos)
    else:
        print("Cantidad de negativos:", negativos)
