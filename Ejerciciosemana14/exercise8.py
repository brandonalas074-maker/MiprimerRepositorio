def buscar_producto(productos, buscar):
    for producto in productos:
        if producto == buscar:
            return "Producto encontrado"
    return "Producto no encontrado"


productos = []
for i in range(5):
    productos.append(input("Ingrese producto: "))

busqueda = input("Buscar producto: ")
print(buscar_producto(productos, busqueda))
