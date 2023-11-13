// Se desea calcular independientemente la suma de los números pares e impares comprendidos entre 1 y 50.
Proceso sin_titulo
	Definir sumas_pares,sumas_impares,i como Enteros;
	sumas_pares <- 0;
	sumas_impares <- 0;
	Para i<-2 Hasta 49 Hacer
		Si i  mod 2 = 0 Entonces
			sumas_pares <- sumas_pares + i;
		SiNo
			sumas_impares <- sumas_impares +i;
		FinSi
	FinPara
	Escribir "La suma pares es:", sumas_pares;
	Escribir "La suma impares es:", sumas_impares	;
FinProceso
