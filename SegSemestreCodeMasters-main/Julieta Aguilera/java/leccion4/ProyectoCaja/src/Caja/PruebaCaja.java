/*
Proyecto caja: 
Ejercicio 1: Crear un proyecto segun especificaciones 
mostradas a continuacion.
La fotma es: Volumen = anchi * alto * profundidad 
 */
package Caja;

public class PruebaCaja {
    public static void main(String[] args) {//metodo void main
        //variables locales 
        int medidaAncho = 6;
        int medidaAlto = 3;
        int medidaProfundidad = 5;
        
        Caja caja1 = new Caja(); //colocamos el objeto, constructor vacio
        caja1.ancho = medidaAncho; //Le pasamos valores al objeto
        caja1.alto = medidaAlto;
        caja1.profundo = medidaProfundidad;
        int resultado = caja1.calcularVolumen(); //Llamamos al metodo
        //Primer resultado
        System.out.println("El resultado de volumen de caja 1: "+resultado);
        
        Caja caja2 = new Caja(4, 4, 2);//Llamamos al contructor 2 con nuevos argumentos
        //Llamamos con el nuevo objeto al metodo para nuevo calculo
        System.out.println("El resultado del volumen de la caja 2: "+caja2.calcularVolumen());
        
        
        
    }
}
