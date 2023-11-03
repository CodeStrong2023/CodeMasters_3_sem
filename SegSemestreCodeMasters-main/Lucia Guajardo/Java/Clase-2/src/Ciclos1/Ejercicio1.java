/*Ejercicio 1: Leer un número y mostrar su cuadrado, 
repetir el proceso hasta que se intoduzca un número negativo.
*/
package Ciclos1;

import javax.swing.JOptionPane;

public class Ejercicio1 {
    public static void main(String[] args) {
        
        int numero, cuadrado;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        while(numero >=0) {
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El número "+numero+" elevado al cuadrado es: "+cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro número: "));
            
        }
        System.out.println("Debe ingresar un número positivo.");
    }
    
}
