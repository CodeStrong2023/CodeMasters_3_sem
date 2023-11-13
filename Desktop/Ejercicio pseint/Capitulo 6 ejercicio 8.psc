// Dada las horas trabajadas de 5 personas
// y la tarifa de pago
// alcular el salario, y la sumatoria de todos los salarios. 
Proceso sin_titulo
	Definir i,horas Como Entero;
	Definir tarifa,salario,suma Como Real;
	i <- 1;
	suma <- 0;
	Mientras i<=5 Hacer
		Escribir "Salario del empleado",i,":";
		Escribir "Digite las horas trabajadas:";
		Leer horas;
		Escribir "Digite las tarifas por horas:";
		Leer tarifa;
		salario <- horas * tarifa ;
		Escribir "El salario es:$",salario;
		suma <- suma + salario;
		i <- i + 1;
		Escribir "";
	FinMientras
	Escribir "La suma den todos lo salarios es:",suma;
FinProceso
