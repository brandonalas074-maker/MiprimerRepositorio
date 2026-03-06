	Algoritmo Ejercicio1_Calificacion
		Definir nota Como Entero
		
		Escribir "Ingrese la nota del estudiante (0 a 10): "
		Leer nota
		
		Si nota < 0 O nota > 10 Entonces
			Escribir "Nota invalida, debe estar entre 0 y 10"
		SiNo
			Si nota >= 6 Entonces
				Escribir "Aprobado"
			SiNo
				Si nota = 5 Entonces
					Escribir "Recuperacion"
				SiNo
					Escribir "Reprobado"
				FinSi
			FinSi
		FinSi
		
FinAlgoritmo
