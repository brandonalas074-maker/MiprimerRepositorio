Algoritmo Ejemplo2
	Definir cajero, cuentaDeAhorro, numeroCuenta, CantidadSaliente, Saldo, preguntar Como Entero
	cuentaDeAhorro = 1000
	numeroCuenta = 12345
	
	Escribir " bienvenido"
	Escribir " Actividad que desea realizar"
	Escribir " 1 para consultar"
	Escribir " 2 para extraer dinero de la cuenta de ahorro"
	
	Escribir " Escriba el numero de cuenta a operar"
	Leer preguntar // yo no quiero ser un uno mejor busco otra chamba
	
	Escribir " Escriba el numero a operar" , preguntar
	//no pueden comenzar con
	//numero
	//signos a menos que sea _
	//no deben llevar espacio
	//Si es una clase siempre inicia con Mayusculas
	// es evitar el cosigo espagueti
	
	//or o puedes llevar
	//panes con cafe o chocolate
	
	//and puedes llevar carne y jamon
	
	//not mejor no
	
	// == si es igual
	//<> diferente ! =
	
	si preguntar == 1
		Escribir " Escriba el numero de cuenta a operar"
		Leer preguntar // es valor de numero de cuentas
		si preguntar == numeroCuenta
			Escribir  "Su saldo es ", cuentaDeAhorro
		FinSi
	FinSi	
		
		si preguntar == 2
			Escribir " Escriba el numero de cuenta a operar"
			Leer preguntar // es valor de numero de cuentas
			si preguntar == numeroCuenta
			
				Escribir "Escriba el monto a extraer "
				Leer preguntar// es lacantidad a extraer	
				// < =
				si preguntar <= cuentaDeAhorro
					Saldo = cuentaDeAhorro - preguntar
					Escribir "Procesando "
					Escribir " Su saldo actual es de" , Saldo
					
				FinSi
		Finsi		
	FinSi
	
FinAlgoritmo
