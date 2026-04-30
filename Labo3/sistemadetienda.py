# Lista de productos (for lo usaremos para mostrarlos)
productos = [
    {"nombre": "Camisa", "precio": 10, "categoria": "ropa"},
    {"nombre": "Pantalón", "precio": 20, "categoria": "ropa"},
    {"nombre": "Calcetines", "precio": 1.5, "categoria": "ropa"},
    {"nombre": "Vestido", "precio": 12, "categoria": "ropa"},
    {"nombre": "Falda", "precio": 5, "categoria": "ropa"},
    {"nombre": "Pan", "precio": 1, "categoria": "comida"},
    {"nombre": "Leche", "precio": 2, "categoria": "comida"},
    {"nombre": "Arroz", "precio": 1.6, "categoria": "comida"},
    {"nombre": "Frijoles", "precio": 1.7, "categoria": "comida"},
]

total = 0

print("BIENVENIDO A LA TIENDA")

# while para seguir comprando
while True:
    print("Productos disponibles:")

    # for para mostrar productos
    for i, producto in enumerate(productos):
        print(f"{i+1}. {producto['nombre']} - ${producto['precio']}")

    opcion = int(input("Elige un producto (número): "))

    if opcion < 1 or opcion > len(productos):
        print("Opción inválida")
        continue

    producto = productos[opcion - 1]

    # select case, en nuestro caso usamos (match-case) para categorías
    match producto["categoria"]:
        case "ropa":
            print("Categoría: Ropa 👕")
        case "comida":
            print("Categoría: Comida 🍞")
        case _:
            print("Otra categoría")

    total += producto["precio"]

    seguir = input("¿Deseas comprar otro producto? (s/n): ").lower()
    if seguir != "s":
        break

# if para descuentos
print("Total sin descuento: $", total)

if total >= 30:
    descuento = total * 0.20
    total -= descuento
    print("Descuento aplicado: 20%")
elif total >= 15:
    descuento = total * 0.10
    total -= descuento
    print("Descuento aplicado: 10%")
else:
    print("No hay descuento")

print("Total a pagar: $", total)
print("Gracias por comprar 🛒")
