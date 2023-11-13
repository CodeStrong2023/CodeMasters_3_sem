Proceso sin_titulo
	Definir letras Como Caracter;
	Dimension letras[100];
	Definir n_elementos,i Como Entero;
	Repetir
		Escribir 'Digite el número de elemntos para el arreglo:';
		Leer n_elementos;
	Hasta Que n_elementos>0
	Para i<-0 Hasta (n_elementos-1) Hacer
		Escribir (i+1),'Digite un numero:';
		Leer letras[i];
	FinPara
	Para i<-(n_elementos-1) Hasta 0 Con Paso -1 Hacer
		Escribir letras[i];
	FinPara
FinProceso
