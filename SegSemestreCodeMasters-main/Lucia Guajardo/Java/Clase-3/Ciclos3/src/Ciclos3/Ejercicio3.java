/*Leer números hasta que se untroduzca un cero.
Para cado uno indicar si es par o impar.
 */
package Ciclos3;

import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese un número:");
        var numero = Integer.parseInt(entrada.nextLine());
        while(numero!=0){
            if(numero % 2 == 0){
                System.out.println("El número "+numero+" es Par.");
            }
            else { 
                System.out.println("El número "+numero+" es Impar.");
            }
            System.out.println("Ingrese otro número: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El número "+numero+" finaliza el programa.");
    }
    
}
