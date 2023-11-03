//: Calcular la suma de los "N" primeros números. 
Proceso sin_titulo
	Definir n, suma, i Como Entero;
	Escribir "Digite algún número"; //5
	Leer n;
	
	suma<- 0;
	Para i<-0 Hasta n Con Paso 1  Hacer
		suma <- suma+i;
	FinPara
	Escribir "La suma de los ", n, " primeros numeros es: ", suma;
FinProceso
