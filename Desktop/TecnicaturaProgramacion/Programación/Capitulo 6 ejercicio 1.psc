//: Calcular la suma de los "N" primeros n�meros. 
Proceso sin_titulo
	Definir n, suma, i Como Entero;
	Escribir "Digite alg�n n�mero"; //5
	Leer n;
	
	suma<- 0;
	Para i<-0 Hasta n Con Paso 1  Hacer
		suma <- suma+i;
	FinPara
	Escribir "La suma de los ", n, " primeros numeros es: ", suma;
FinProceso
