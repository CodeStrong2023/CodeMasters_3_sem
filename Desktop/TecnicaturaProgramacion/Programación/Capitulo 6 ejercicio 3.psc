Proceso sin_titulo
	Definir num, i como enteros;
	Definir conteo_positivo,conteo_negativo,conteo_neutro como enteros;
	conteo_positivo <- 0;
			conteo_negativo<-0;
	conteo_neutro <- 0;
	Para i<-1 Hasta 10 Hacer
		Escribir i,"Digite un número:";
		Leer num;
		Si num = 0 Entonces
			conteo_neutro <- conteo_neutro +1;
		SiNo
			Si num>0 Entonces
				conteo_positivo <- conteo_positivo+1;
			SiNo
				conteo_negativo <- conteo_negativo+1;
			FinSi
		FinSi
	FinPara
	Escribir "La cantidad de positivos es:",conteo_positivo;
	Escribir "La cantidad de negativos es:",conteo_negativo;
	Escribir "La cantidad de neutro es:", conteo_neutro;
FinProceso
