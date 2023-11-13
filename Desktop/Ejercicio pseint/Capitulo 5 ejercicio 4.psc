//Leer dos números, si son iguales que los multiplique
//si el primero es mayor que el segundo que los reste
// y si no que los sume 
Proceso sin_titulo
	Definir num1,num2 Como Real;
	Escribir "Digite dos números:";
	Leer num1,num2;
	Si num1=num2 Entonces
		resultado<- num1*num2;
	finsi
		
	Si	num1 > num2 Entonces
		resultado<- num1-num2;
	SiNo
		resultado<- num1+num2;
	FinSi
	Escribir "El resultado es;" , resultado;
FinProceso
