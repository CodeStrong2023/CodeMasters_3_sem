Algoritmo sin_titulo
	Definir kil�metros Como Entero;
	Escribir "Ingrese el n�mero de kil�metros:";
	Leer kil�metros;
	si kil�metros== 300 Entonces
		Escribir kil�metros,"El monto fijo ser� de 3000 pesos:";
	SiNo
		si kil�metros>300 Entonces
			Escribir "Pagar adicional de 150 m�s IVA por cada kil�metro en exceso de 300:";
		SiNo
			si kil�metros>1000 Entonces
				Escribir "Pagar monto adicional de 100 pesos m�s IVA po cada kil�metro en exceso de 1000:";
			FinSi
		FinSi
	FinSi
FinAlgoritmo
