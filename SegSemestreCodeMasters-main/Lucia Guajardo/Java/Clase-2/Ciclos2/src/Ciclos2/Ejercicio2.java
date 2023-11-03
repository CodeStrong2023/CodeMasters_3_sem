/*Leer un número e indicar si es positivo o negativo.
El proceso se repetira hasta que se introduzca un cero.
 */
package Ciclos2;

import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese un número:");
        var numero = Integer.parseInt(entrada.nextLine());
        while(numero!=0){
            if(numero > 0){
                System.out.println("El número "+numero+" es Positivo.");
            }
            else { 
                System.out.println("El número "+numero+" es Negativo.");
            }
            System.out.println("Ingrese otro número: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El número "+numero+" finaliza el programa.");
    }
}
