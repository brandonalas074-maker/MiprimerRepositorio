# las comillas triples son las que se encargan de hacer
# Cadenas de texto largas sin modificar el formato.
# 2 comillas: para texto corto
# 3 " ": para texto largo
poema = ""
music = """ Ya no me alcanza la razón / Ya no me importa el mundo sin ella / 
Ella es el sueño de un perdedor /
 Que la encontró / Y ahora puede existir"""

# print(poema)

##computadora -> que variable queres imprimir
## como sabe, por el metodo "print"
# print() -> es la función que se encarga de imprimir pantalla
# void -> no devuelve nada
# objeto -> devuelve un tipo de dato


# realizar una wiki, tambien se puede ver dando doble clic
# en el documeto y se les despelga el editor de texto

## esa canción a mayusculas
## mutabilidad -> siempre debemos evitar transformar objeto original
## clases -> estereotipo ( defini: como un  molde)
## estan formadas por propiedades ->

## music es un espacio de memoria para string
## se va a llenar con el contenido de music
music_Mayusculas = music.upper()
print(music_Mayusculas)

## convertir en minisculas
## string .lower

music_minuscula = music.lower()
print(music_minuscula)

## tiene que ingresar 100 nombres en mayuscula
mensaje = "hOlA kACe progRMando o qUe HaCe"
## Capitalize a que la primera letra de cada palabra sea mayuscula
mensajeCorrecto = mensaje.capitalize()
print(mensajeCorrecto)

## Las flipantes aventuras de el gato con bolson magico y alfredo
titulo = "Las flipantes aventuras de el gato con bolson magico y alfredo"
tituloCorrecto = titulo.title()
print(tituloCorrecto)


## swapCase() permite cambiar entre mayusuculas y minusculas
swapCaseTitulo = tituloCorrecto.swapcase()
print(swapCaseTitulo)
