Proceso sin_titulo
	Definir nElementos como entero;
	pedirDatos(nElementos);
	mostrarSerie(nElementos);
FinProceso

SubProceso pedirDatos(nElementos por referencia)
	Escribir sin saltar "Digite el número de elementos:";
	Leer nElementos;
FinSubProceso

SubProceso mostrarSerie(nElementos)
	Definir i como entero;
	Escribir "";
	Escribir "La serie fibonacci es:";
	Escribir Sin saltar " 0";
	Para i<-1 Hasta nElementos-1 Hacer
		Escribir Sin saltar fibonacci(i)," ";
	FinPara
FinSubProceso

SubProceso retorno <- fibonacci(num)
	Definir retorno como entero;
	Si num = 1 o num = 2 Entonces
		retorno <- 1;
	SiNo
		Retorno <- fibonacci(num-1) + fibonacci(num-2);
	FinSi
FinSubProceso
