/*Ejercicio 3:
Leer 5 números por teclado, almacenarlos en un arreglo y a continuación
realizar la media de los números positivos, la media de los negativos y contar
el número de ceros.
 */
package ejercicio3;

import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float[] numeros = new float[5];
        float negativos=0, positivos=0, mediaNegativos, mediaPositivos;
        int conteo0=0; 
        int conteoNegativos = 0;
        int conteoPositivos = 0;
        
          for(int i=0; i<5; i++) {
            System.out.println("Ingrese un número: ");
            numeros[i] = entrada.nextFloat();
            if(numeros[i]>0) {
                positivos += numeros[i];
                conteoPositivos++;
            }
            else if(numeros[i]<0) {
                negativos += numeros[i];
                conteoNegativos++;
            }
            else {
                conteo0++;
            }
          }
          
          if(conteoPositivos == 0) {
              System.out.println("\nNo se ouede sacar la media de los números positivos. ");
          }
          else {
              mediaPositivos = positivos/conteoPositivos;
              System.out.println("\nLa media de los números positivios es: "+mediaPositivos);
          }
          
         if(conteoNegativos == 0) {
              System.out.println("\nNo se ouede sacar la media de los números negativos. ");
          }
          else {
              mediaNegativos = negativos/conteoNegativos;
              System.out.println("\nLa media de los números positivios es: "+mediaNegativos);
          }
         
         System.out.println("La cantidad de ceros es: "+conteo0);
    }
    
}
