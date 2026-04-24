impares = []
suma = 0

while True:
    num = int(input("Ingresa un número (0 para salir): "))
    if num == 0:
        break
    if num % 2 != 0:
        impares.append(num)
        suma += num

print("Suma de impares:", suma)
for i in impares:
    print("Número impar ingresado:", i)
