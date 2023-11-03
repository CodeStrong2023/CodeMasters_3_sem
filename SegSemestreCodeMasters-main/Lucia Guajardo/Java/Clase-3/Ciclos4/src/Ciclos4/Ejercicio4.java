/*Pedir números hasta que se teclee uno negativo,
y mostrar cuántos números se han introducido. 
 */
package Ciclos4;

import java.util.Scanner;

public class Ejercicio4 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0;
        System.out.println("Ingrese un número: ");
        numero = Integer.parseInt(entrada.nextLine());
        while (numero >= 0) {
            System.out.println("El número "+numero+" es Positivo.");
            conteo++;
            System.out.println("Ingrese otro número: ");
             numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("Se han ingresado "+conteo+" números que no son negativos.");
    }
    
}
