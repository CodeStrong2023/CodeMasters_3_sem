/*Pedir numeros hasta que se teclee un 0,
mostrar la suma de todo los números introducidos.
 */
package Ciclos6;

import java.util.Scanner;

public class Ejercicio6 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, suma = 0;
        do{
            System.out.println("Ingrese un número: ");
            numero = Integer.parseInt(entrada.nextLine());
            suma+= numero;
        }while(numero != 0);
        System.out.println("La suma de los números ingresados es: "+suma);
    }
    
}
