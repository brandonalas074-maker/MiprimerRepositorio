Algoritmo Ejercicio4división
	Definir numero1,numero2, division Como Real
	Escribir "Ingrese su numero para dividir"
	Leer numero1
	
	Escribir "Ingrese su otro numero para poder dividir"
	Leer numero2
	
	Si numero2 <> 0 Entonces
		resultado = numero1 / numero2
		
		Escribir "El resultado de la respectiva división es",resultado
		
	SiNo
		Escribir "Error: No se puede dividir entre cero"
	FinSi
	
FinAlgoritmo
