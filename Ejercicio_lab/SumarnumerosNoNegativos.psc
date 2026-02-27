Algoritmo SumarnumerosNoNegativos
	
		Definir numero Como Real
		Definir suma Como Real
		Definir continuar Como Logico
		
		suma <- 0
		continuar <- Verdadero
		
		Repetir
			
			
			Escribir "Ingrese cualquier número:"
			Leer numero
			
			// Validamos con NO para verificar que no sea negativo
			Si NO (numero < 0) Entonces
				suma <- suma + numero
				Escribir "número agregado."
			SiNo
				Escribir "número negativo, no se suma."
			FinSi
			
			Escribir "¿Desea continuar? (Verdadero/Falso):"
			Leer continuar
			
		Hasta Que No continuar
		
	      Escribir "La suma total es: ", suma
		
		
FinAlgoritmo

