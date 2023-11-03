Algoritmo sin_titulo
	Definir kmRecorrido,MontoaPagar,Montoiva,iva Como Real;
	Definir MontoFijo Como Entero
	MontoFijo= 3000;
	iva= 0.20;
	Escribir "Ingrese los km que ha recorrido:";
	Leer kmRecorrido;
	si  kmRecorrido<= 300 Entonces
		MontoaPagar= MontoFijo;
	SiNo
		si kmRecorrido<= 1000 Entonces
			MontoaPagar= MontoFijo+150 *(kmRecorrido-300)
		SiNo
			si kmRecorrido<= 1000 Entonces
				MontoaPagar= MontoFijo+150+700+100+(kmRecorrido-1000)
			
			finsi
			FinSi
			Montoiva= Iva *(MontoaPagar+MontoFijo)
	FinSi
	Escribir "El monto a pagar es de $:",MontoaPagar;
	Escribir "El iva será de $:",Montoiva;
FinAlgoritmo
