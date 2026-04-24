import random

secreto = random.randint(1, 20)
intentos = []

while True:
    num = int(input("Adivina el número:"))
    intentos.append(num)
    if num == secreto:
        print("¡Correcto! El número secreto era:", secreto)
        break
    elif num < secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")

for i in intentos:
    print("Intento:", i)
