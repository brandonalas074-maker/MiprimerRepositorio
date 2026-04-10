palabra = "CANTANDO"
minusculas = palabra.lower()
sin_sufijo = minusculas.removesuffix("ando")
posicion_t = sin_sufijo.find("t")

print("En minúsculas:", minusculas)
print("Sin sufijo:", sin_sufijo)
print("Posición de 't':", posicion_t)
