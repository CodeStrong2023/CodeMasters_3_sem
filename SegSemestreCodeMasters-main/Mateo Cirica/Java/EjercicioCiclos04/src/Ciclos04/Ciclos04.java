/*
 * Ejercicio 4: Pedir numeros hasta que se teclee uno negativo,
 * y mostrar cuantos numeros se han introducido.
 * Lo hacemos primero con la clase Scanner 
 * Luego lo hacemos con la JOptionPane
 */
package Ciclos04;

import java.util.Scanner;

public class Ciclos04 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0){
            System.out.println("El numero ingresado es: "+numero);
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El numero ingresado ("+numero+") finaliza el programa");
    }
}
