Proceso Cadena_de_Caracteres
	Definir i Como Entero;
	Definir frase,frase2,fraseRevez como cadenas;
	
	
	Escribir 'digite una cadena: ';
	Leer frase;
	
	i <- 0;
	frase2 <- '';
	
	
	
	Mientras i<Longitud(frase) Hacer
		si Subcadena(frase,i,i) <> '' Entonces
			frase2 <- Concatenar(frase2,SubCadena(frase,i,i));
			i <- i + 1;
		SiNo
			i <- i + 1;
		FinSi
	FinMientras
	
	frase <- frase2;
	
	
	fraseRevez <- '';
	Para i<-(Longitud(frase)-1) Hasta 0 con paso -1 Hacer
		fraseRevez <- Concatenar(fraseRevez,SubCadena(frase,i,i));
	FinPara
	
	
	
	si frase = fraseRevez Entonces
		Escribir 'la cadena es un palindromo: ',frase;
	SiNo
		Escribir 'la cadena NO es una palindromo: ',frase;
		
	FinSi
FinProceso
