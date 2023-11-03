/*
Proyecto caja:
Ejercicio 1:Crear un proyecto según las especificaciones
mostradas a continuacíon.
La formula es: volumen= ancho*alto*profundidad
*/
package caja;

public class PruebaCaja {
    public static void main(String[] args) {
        //variables locales
        int medidaAncho = 3;//valores ingresados en código duro
        int medidaAlto = 2;
        int medidaProfu = 6;
        
        Caja caja1 = new Caja();//Instancamos el objeto, constructor vacio
        caja1.ancho = medidaAncho;//Le pasamos los valores al objeto
        caja1.alto = medidaAlto;
        caja1.profundo = medidaProfu;
        int resultado = caja1.calcularVolumen();//Llamamos al método
        //Primer resultado
        System.out.println("Resultado volumen en caja 1: "+resultado);
        
        Caja caja2 = new Caja(2, 4, 6);//Llamamos al constructor 2 con nuevos argumentos
        //Llamamos con el nuevo objeto al método para un nuevo calculo
        System.out.println("resultado volumen de caja 2: "+caja2.calcularVolumen());
    }
    
}
