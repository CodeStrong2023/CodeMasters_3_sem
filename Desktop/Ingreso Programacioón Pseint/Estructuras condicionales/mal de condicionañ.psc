Algoritmo sin_titulo
	Definir kilómetros Como Entero;
	Escribir "Ingrese el número de kilómetros:";
	Leer kilómetros;
	si kilómetros== 300 Entonces
		Escribir kilómetros,"El monto fijo será de 3000 pesos:";
	SiNo
		si kilómetros>300 Entonces
			Escribir "Pagar adicional de 150 más IVA por cada kilómetro en exceso de 300:";
		SiNo
			si kilómetros>1000 Entonces
				Escribir "Pagar monto adicional de 100 pesos más IVA po cada kilómetro en exceso de 1000:";
			FinSi
		FinSi
	FinSi
FinAlgoritmo
