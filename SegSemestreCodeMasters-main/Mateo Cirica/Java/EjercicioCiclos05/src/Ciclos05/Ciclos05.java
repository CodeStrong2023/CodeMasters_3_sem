/*
 * Ejercicio 5: Realizar un juego para adivinar un numero,
 * para ello generar un numero aleatorio entre 0-100, y
 * luego ir pidiendo numeros indicando "es mayor" o
 * "es menor" segun sea mayor o menos con respecto a N
 * El proceso termina cuando el usuario acierta y mostramos
 * el numero de intentos hechos
 */
package Ciclos05;

import java.util.Scanner;

import javax.tools.Diagnostic;

public class Ciclos05 {

    public static void main(String[] args) {
        Scanner entrance = new Scanner(System.in);
        int numero, aleatorio, conteo = 0;
        aleatorio = (int) (Math.random() * 100);
        do {
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(entrance.nextLine());
            if(numero < aleatorio){
                System.out.println("Digite un numero mayor");
            }
            else if(numero > aleatorio){
                System.out.println("Digite un numero menor");
            }
            else{
                System.out.println("¡¡¡FELICIDADES!!! Has adivinado el numero");
            }
            conteo++;
        }while(numero != aleatorio);
        System.out.println("Adivinaste el numero en: "+conteo+" intentos");
        }

    }
