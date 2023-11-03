/*Ejercicio 2:
Leer 5 números, guardarlos en un arreglo y mostrarlos en el orden inverso al introducirlos.
 */
package ejercicio2;

import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float[] numeros = new float[5];
        
         for(int i=0; i<5; i++) {
             System.out.println("Ingrese un número: ");
            numeros[i] = entrada.nextFloat();
         }
         
         for(int i=4; i>=0; i--) {
             System.out.println(i+" "+numeros[i]);
    }
         System.out.println("\n");
    }
    
}
