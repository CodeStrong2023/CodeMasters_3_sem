Proceso sin_titu
	Definir  suma,csumin,csumpar,sumar Como Entero;
	escribir "determine cuantos de sus numeros son pares";
	
	sumar<-0;
	
	suma<-0;
	
	csumin<-0;
	
	csumpar<-0;
	
	Para s<-1 Hasta 10 Con Paso 1 Hacer
		
		escribir "ingrese numero ",s,"";
		
		leer n;
		
		Si n%2=0 Entonces
			
			csumpar<- csumpar + 1;
			
			sumar<- sumar + n;
			
		Sino
			
			csumin<- csumin + 1;
			
			suma<- suma + n;
		FinSi
		
		FinPara
		
	
	escribir "sus numeros pares son:",csumpar;
	
	escribir "la suma de los numeros pares es:",sumar;
	
	escribir "sus numeros impares son:",csumin;
	
	escribir "la suma de los numeros impares es:",suma;
	
	escribir "el promedio de los numeros impares es:",suma/10;
FinProceso
