Funcion respuesta <- validar ( usuario, pass )
	respuesta = Falso
	Escribir "Validar usuario"
	Si usuario == "Brandish" Entonces
		Si pass == "brandon"  Entonces
			Escribir "Bienvenido"
			respuesta = Verdadero
		SiNo
			Escribir "Fallo de password"
			respuesta = Falso
		FinSi
	SiNo
		Escribir "Fallo de usuario"
		
	FinSi
	
FinFuncion
//cuando se crea una funcion 
//encapsulación -> siempre me va a dar la misma salida
//va a crear algo que se llama scope
//scope: se refiere al contexto

// las vaariables siempre tiene que tener sentido
// edad =32 funcion <- registrar persona (edad)
//funcion <-  registrar persona (xw)
// nombre en clave de las variables , no. nombre de ex, nombres,
//personajes, fechas...
// xw = "Hola com estas"
// nomeclatura camelCase y sneskCase
//glosario
//ADN 

Algoritmo  bucleFor
	//indica que vamos a repetir los pasos o un
	//algoritmo en un numero de pasos
	
	//yo quiero utilizar la cuenta de correo
	//pero si me equivoco mas de 4 veces
	//se boquea momentamente
	
	
	Definir   increment Como Entero
	Escribir "registrar usuario"
	leer usuario
	
	Escribir "registrar PASS"
	leer pass
	
	respuesta = validar ( usuario ,pass)
	
	Escribir respuesta
	// funcion es una estrucutura de codigo que se puede
	//repetir pero siempre se llama a la misma instancia
	//bajo el mismo nombre
	
	//palabra reservada.. si nos devuelve algo () 
	//los argumentos iran dentro () argumento es: son las entradas de las funciones
	//y pueden ser más de una o ninguna.
	//caracteristica -> el carro es rojo
	//nosotros somos guapos
	//edad, numero, boolean , verdadero o falso
	//objeto 		un objeto: es aquella entidad en programación
	//		que modela en base a las clases, las caracteristicas de un objeto
	//			en la vida real
	
	Definir i Como Entero
	resultado = validar ( usuario, pass)
	Para i <- 0 Hasta 5 Con Paso 1 Hacer

		si resultado == Verdadero
			Escribir "Bienvenida"
			Escribir "Indicaciones"
		FinSi
		resultado = falso
	FinPara
	
	//for i = 0 ; instruccionlogica i> 20;
	// i = i + 1 ...19 detener el bucle
	
	
FinAlgoritmo
