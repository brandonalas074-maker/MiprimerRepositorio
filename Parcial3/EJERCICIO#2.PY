from decimal import Decimal

total = Decimal("0")

while True:
    try:
        precio = Decimal(
            input("Ingrese el precio del producto (oprime 0 para salir): ")
        )

        if precio == 0:
            break

        total += precio

    except ValueError:
        print("Advertencia: Debe ingresar un número válido")

    except:
        print("Entrada inválida")

print(f"Total acumulado: ${total}")
