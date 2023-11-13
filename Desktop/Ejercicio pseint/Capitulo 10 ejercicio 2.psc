Proceso sin_titulo
	definir frase1, frase2 como caracter;
	Escribir "Digite una cadena";
	Leer frase1;
	Escribir "Digite otra cadena";
	Leer frase2;
	Escribir "";
	Si longitud(frase1)= longitud(frase2) Entonces
		Escribir "Ambas tienen la misma longitud";
	SiNo
		Si longitud(frase1)> longitud(frase2) Entonces
			Escribir frase1;
			Escribir "Su longitud es:",longitud(frase1)	;
		SiNo
			Escribir frase2;
			Escribir "Su longitud es:", longitud(frase2);
		FinSi
	FinSi
FinProceso
