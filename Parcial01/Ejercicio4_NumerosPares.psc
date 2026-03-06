Algoritmo Ejercicio4_NumerosPares
    Definir N, i Como Entero
    
    Escribir "Ingrese cuantos numeros pares desea mostrar:"
    Leer N
    
    Si N <= 0 Entonces
        Escribir "Error: el numero debe ser mayor que 0"
    SiNo
        Para i <- 1 Hasta N Hacer
            Escribir i * 2
        FinPara
    FinSi
    
FinAlgoritmo
