Algoritmo sin_titulo
	Definir num, iterador Como Entero
	Definir haynegativo Como Logico;
	Para i <- 1 Hasta 5 Con Paso 1 Hacer
		Escribir "Ingresa un n�mero;";
		Leer num;
		Si num < 0 Entonces
			haynegativo= Verdadero
		FinSi
		
	Fin Para
	si haynegativo Entonces
		Escribir "Hay n�meros negativos:";
	SiNo
	Escribir "No hay n�meros negativos:";
		
	FinSi
FinAlgoritmo
