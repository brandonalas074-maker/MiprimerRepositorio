for numero in range(1, 51):

    # Saltar el múltiplos de 3
    if numero % 3 == 0:
        continue

    # Detener en 42
    if numero == 42:
        print("Amenaza detectada")
        break

    print(f"Procesando registro ID: {numero}")
