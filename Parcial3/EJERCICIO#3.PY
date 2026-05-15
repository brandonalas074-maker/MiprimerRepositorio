temperaturas = []

# Solicitaremos 5 temperaturas
for i in range(5):
    temp = int(input(f"Ingrese la temperatura #{i + 1}: "))
    temperaturas.append(temp)

# Evaluaamos temperaturas
for temperatura in temperaturas:

    match temperatura:

        case 0:
            print("Alerta: Punto de Congelación")

        case 100:
            print("Alerta: Punto de Ebullición")

        # Temperaturas menores a 0, ----> para poder evaluar también bajo cero
        case _ if temperatura < 0:
            print("Estado Crítico: Congelación Extrema")

        case _:
            estado = "Estado: Estable" if 10 <= temperatura <= 30 else "Estado: Crítico"
            print(estado)
