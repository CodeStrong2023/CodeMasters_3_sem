/*Ejercicio 1: Crear un proyecto según las especificaciones
mostradas a continuación.
La formula es: volúmen = ancho * alto * profundidad.
 */
package caja;


public class PruebaCaja {
    public static void main(String[] args) {
        int medidaAncho =3;
        int medidaAlto = 2;
        int medidaProf = 6;
        
        Caja caja1 = new Caja();
        caja1.ancho = medidaAncho;
        caja1.alto = medidaAlto;
        caja1.profundidad = medidaProf;
        int resultado = caja1.calcularVolumen();
        System.out.println("Volúmen de caja 1: "+resultado);
        
        Caja caja2 = new Caja(2, 4, 6);
        System.out.println("Volúmen de caja 2:"+ caja2.calcularVolumen());
    }
    
}
