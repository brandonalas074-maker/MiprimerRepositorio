def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


while True:
    n = int(input("Ingresa un numero (0 para salir): "))
    if n == 0:
        break
    for i in range(1, n + 1):
        if es_primo(i):
            print(i)
