Proceso sin_titulo
		definir mayor,menor como reales;
		definir n_elementos,i como enteros;
		definir num como real;
		dimension num[100];
		Repetir
			Escribir 'Digite el numero de elementos para el arreglo: ';
			Leer n_elementos;
		Hasta Que n_elementos > 0
		Para i<-0 Hasta  (n_elementos-1) Hacer
			Escribir (i+1),' . digite un numero: ';
			Leer num[i];
		FinPara
		mayor <- num[0];
		menor <- num[0];
		Para i<-1 Hasta (n_elementos-1) Hacer
			Si num[i] > mayor Entonces
				mayor <- num[i];
			SiNo
				Si num[i] < menor Entonces
					menor <- num[i];
				FinSi
			FinSi
		FinPara
		Escribir 'el numero mayo es: ', mayor;
		Escribir 'el numero menor es: ', menor;
FinProceso

