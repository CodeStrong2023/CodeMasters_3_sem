
SubProceso pedirDatos(base Por Referencia, exponente Por Referencia)
	Escribir Sin Saltar"Digite una base:";
	Leer base;
	Escribir Sin Saltar"Digite un exponente:";
	Leer exponente;
FinSubProceso
Funcion retorno <- potencia(base,exponente)
	Definir retorno como entero;
	Si exponente = 0 Entonces
		retorno<- 1;
	SiNo
		retorno<- base * potencia(base,exponente-1);
	FinSi
FinFuncion
Proceso sin_titulo
	Definir base,exponente Como Entero;
	pedirDatos(base,exponente);
Escribir "La potencia es:",potencia(base,exponente);
FinProceso
