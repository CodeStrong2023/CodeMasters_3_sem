Algoritmo sin_titulo
	Definir num, iterador Como Entero
	Definir haynegativo Como Logico;
	Para i <- 1 Hasta 5 Con Paso 1 Hacer
		Escribir "Ingresa un número;";
		Leer num;
		Si num < 0 Entonces
			haynegativo= Verdadero
		FinSi
		
	Fin Para
	si haynegativo Entonces
		Escribir "Hay números negativos:";
	SiNo
	Escribir "No hay números negativos:";
		
	FinSi
FinAlgoritmo
