Proceso Principal
	definir apellidos como cadena;
	dimension apellidos[5];
	pedirdatos(apellidos);
	ordenar(apellidos);
	mostrardatos(apellidos);
	Escribir '';
FinProceso

SubProceso pedirdatos(apellidos por referencia)
	Definir i como entero;
	Para i<-0 Hasta 4 Hacer
		Escribir sin saltar (i+1),'. digite un apellido: ';
		Leer apellidos[i];
	FinPara
FinSubProceso

SubProceso ordenar(apellidos por referencia)
	definir i,j como entero;
	definir aux como cadena;
	Para i<-0 Hasta 3 Hacer
		Para j<-0 Hasta 3 Hacer
			Si apellidos[j] > apellidos[j+1] Entonces
				aux <- apellidos[j];
				apellidos[j] <- apellidos[j+1];
				apellidos[j+1] <- aux;
			FinSi
		FinPara
	FinPara
FinSubProceso

SubProceso mostrardatos(apellidos)
	definir i como entero;
	Escribir '';
	Escribir 'los apellidos ordenados alfabeticamente son: ';
	Para i<-0 Hasta 4 Hacer
		Escribir (i+1),'. ',apellidos[i];
	FinPara
FinSubProceso
