while True:
    monto = float(input("Monto de compra: "))

    if monto >= 0:
        break
    else:
        print("Monto inválido")

if monto > 100:
    descuento = monto * 0.20
elif monto >= 50:
    descuento = monto * 0.10
else:
    descuento = 0

print("Total:", monto - descuento)
