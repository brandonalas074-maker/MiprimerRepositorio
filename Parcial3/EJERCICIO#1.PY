# Ejercicio 1

etiqueta = input("Ingrese la etiqueta de rastreo: ")

# Validación de seguridad
if etiqueta == "" or etiqueta is None:
    print("Error: entrada vacía")
else:
    # Extraer categoría usando slicing
    partes = etiqueta.split("-")
    categoria = partes[1]

    print(f"Categoría: {categoria}")

    # Operador ternario
    ruta = "Ruta Local" if etiqueta.endswith("SV") else "Ruta Internacional"

    print(ruta)
