/*
Ejercicio 5: Realizar un juego para adivinar un numero,
para ello generar un numero aleatorio entre 0-100, y
luego ir pidiendo numero indicando "es mayoe" o "es menor"
seun sea mayor o menor con respecto a n
El proceso termina cuando el usuario acierta y mostramos 
el numero de intentos
 */
package Ciclos05;

import java.util.Scanner;

public class Ciclos05 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, aleatorio, contador = 0;
        aleatorio = (int)(Math.random()*100); //Esto genera un numero aleatorio
        do{
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            if(numero <aleatorio){
                System.out.println("Digite un numero mayor: ");    
            }
            else if(numero > aleatorio){
                System.out.println("Digite un numero menor: ");
            }
            else{
                System.out.println("¡Felicidades! Has adivinado el numero ");
            }
            contador++;   
        }while(numero != aleatorio);
        System.out.println("Adivinaste el numero en "+contador+ "intentos");
    }
}
