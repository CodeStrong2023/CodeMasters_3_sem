Proceso cdlol
	Definir opcion Como Entero;
	Escribir 'MENU';
	Escribir '1.Elevar un n�mero a una potencia x';
	Escribir '2.Sacar la ra�z cuadrada de un n�mero';
	Escribir '3. Salir';
	Escribir 'Digite una opci�n';
	Leer opcion;
	Segun opcion  Hacer
		1:
			Definir num,potencia,rdo Como Real;
			Escribir 'Digite un n�mero';
			Leer num;
			Escribir 'Digite la potencia';
			Leer potencia;
			rdo <- num^potencia;
			Escribir "El resultado es:",rdo;
		2:
			Definir num,resultado como reales;
			Escribir "Digite un n�mero";
			Leer num;
			resultado <- rc(num);
			Escribir "El resultado es:",resultado;
		3:
		De Otro Modo:
			Escribir "Se equivoco de opcion de menu";
	FinSegun
FinProceso
