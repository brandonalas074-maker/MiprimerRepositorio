cadena = "Python2026"
alfanumerico = cadena.isalnum()

if alfanumerico:
    minusculas = cadena.lower()
    separado = minusculas.replace("2026", "")
    print("Es alfanumérico:", alfanumerico)
    print("En minúsculas:", minusculas)
    print("Separado:", separado)
else:
    print("No es alfanumérico")
