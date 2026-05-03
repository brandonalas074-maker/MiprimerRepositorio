def promedio_notas(notas):
    promedio = sum(notas) / len(notas)

    if promedio >= 6:
        estado = "Aprueba"
    else:
        estado = "Reprueba"

    return promedio, estado


notas = [7, 9, 10, 6]
print(promedio_notas(notas))
