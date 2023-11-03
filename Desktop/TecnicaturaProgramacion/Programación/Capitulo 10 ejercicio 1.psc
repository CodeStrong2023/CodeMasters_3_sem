//Diseñe un programa que permita ingresar una cadena de caracteres, y detecte cuántas vocales tiene. 
Proceso sin_titulo
	Definir i,j,conteoVocales Como Entero;;
	Definir frase, vocales Como cadenas;
	Escribir Sin Saltar"Digite una cadena";
	leer frase;
	frase<- Minusculas(frase);
	vocales<- "aeiou";
	conteoVocales<- 0;
	Para i<- 0 Hasta (Longitud(frase)-1) Con Paso 1 Hacer
		Para j <- 0 hasta (Longitud(vocales)-1) Con Paso 1 Hacer
			
			si (SubCadena(frase,i,i) = SubCadena(vocales,j,j) )Entonces
				conteoVocales<- conteoVocales+1;
				
			FinSi
		FinPara
	FinPara
	Escribir "El número de la cadena es:",conteoVocales;
FinProceso
