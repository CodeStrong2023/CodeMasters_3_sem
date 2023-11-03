Proceso sin_titulo
	Definir parcial1,parcial2,parcial3,promedioP,notasParcial como reales;
	Definir examen_final,notaExamen como reales;
	Definir notaTrabajo,notaFinalTrabajo como reales;
	Definir notaFinal como real;
	Escribir "Digite las 3 notas de los parciales";
	Leer parcial1,parcial2,parcial3;
	promedioP <- (parcial1+parcial2+parcial3)/3;
	notasParcial <- promedioP*0.55;
	Escribir "Digite la nota del examen final: ";
	Leer examen_final;
	notaExamen <- examen_final *0.3;
	Escribir "Digite la nota del trabajo final: ";
	Leer notaTrabajo;
	notaFinalTrabajo <- notaTrabajo * 0.15;
	notaFinal <- notasParcial+notaExamen+notaFinalTrabajo;
	Escribir "La calificaciónfinal es: ",notaFinal;
FinProceso
