// En un alamcén se hace el 20 MOD  de descuentokl
// A los clientes cuya compra supere los 100 pesos.
// ¿Cuál será la cantidad que pagará la persona por su compra?
Proceso sin_titulo
	Definir compra,descuento,precio_final como Real;
	Escribir "Digite la cantidad a pagar:";
	Leer compra;
	Si compra> 100 Entonces
		descuento <- compra* 0.2;
	SiNo
		descuento <- 0;
	FinSi
	precio_final <- compra- descuento;
	Escribir "El precio final es:", precio_final;
FinProceso
