numeros_validos = []
suma = 0

while suma <= 100:
    num = int(input("Ingresa un número:"))
    if num < 0:
        continue
    numeros_validos.append(num)
    suma += num

print("La suma superó 100.")
for n in numeros_validos:
    print("Número válido ingresado:", n)
