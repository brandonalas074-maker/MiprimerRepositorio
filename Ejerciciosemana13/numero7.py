notas = []

while True:
    nota = float(input("Ingresa una nota (-1 para ver el resultado):"))
    if nota == -1:
        break
    if 0 <= nota <= 10:
        notas.append(nota)

suma = 0
for n in notas:
    suma += n

if len(notas) > 0:
    promedio = suma / len(notas)
    print("Promedio de notas válidas:", promedio)
else:
    print("No se ingresaron notas válidas.")
