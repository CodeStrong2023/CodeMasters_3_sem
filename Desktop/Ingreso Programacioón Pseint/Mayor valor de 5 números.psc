Algoritmo sin_titulo
	Definir n1,n2,n3,n4,n5 Como Entero;
	Definir mayor_valor Como Entero;
	Escribir "ingrese el primer n�mero:";
	Leer n1;
	Escribir "ingrese el segundo n�mero:";
	Leer n2;
	Escribir "ingrese el tercer n�mero:";
	Leer n3;
	Escribir "ingrese el cuarto n�mero:";
	Leer n4;
	Escribir "ingrese el quinto n�mero:";
	Leer n5;
	
	mayor_valor = 0;
	
	Si mayor_valor< n1 Entonces
		
		mayor_valor = n1
	Fin Si
	
	Si n1< n2 Entonces
		
		mayor_valor = n2
	Fin Si
	
	Si n2< n3 Entonces
		
		mayor_valor = n3
	Fin Si
	
	Si n3<n4 Entonces
		
		mayor_valor = n4
	Fin Si
	
	Si n4< n5 Entonces
		
		mayor_valor = n5
	Fin Si
	
	Escribir "El mayor valor es:",mayor_valor;
FinAlgoritmo
