nota = int(input("Ingresa una calificación (0-10): "))

if 9 <= nota <= 10:
    print("Excelente")
elif 7 <= nota <= 8:
    print("Bueno")
elif nota == 6:
    print("Aprobado")
elif 0 <= nota <= 5:
    print("Reprobado")
else:
    print("Nota inválida")
