
package proyecto_memoria;

import java.util.Scanner;
import java.util.Random;

public class Proyecto_memoria {
    public static void main(String[] args) {
         Scanner entrada = new Scanner(System.in);
         System.out.println("***********************************");
         System.out.println("¡Bienvenido al juego de memoria!");
         System.out.println("***********************************");
         System.out.println();
         System.out.println("Para ganar necesitas una puntuación igual o mayor a 3.");
         System.out.println();
         System.out.println("Los puntos se consiguen adivinando bien los números y sus posiciones dados en pantalla.");
         System.out.println();
         System.out.println("¡Buena suerte, espero que lo disfrutes :D!");
         System.out.println();
         
         int[] numeros_al_azar = new int[5];
         int puntaje = 0;
         
         Random generadorAleatorio = new Random();
         
         for (int i = 0; i < 5; i++) {
            int numeroAleatorio = generadorAleatorio.nextInt(100); // Genera un número aleatorio entre 0 y 99
            numeros_al_azar[i] = numeroAleatorio; 
         }
            
         for (int i = 0; i < 5; i++) {
            System.out.println("Número " + (i + 1) + ": " + numeros_al_azar[i]);}
         
         System.out.println();
         System.out.println("Cuando estés listo escribe 'si': ");
         var opc = entrada.next();
         
         if (opc.equals("si")) {
             
             for (int i = 0; i < 50; i++) {
                   System.out.println();
             }
         }
         
         
           for (int j = 0; j < 5; j++) {
               System.out.println("Ingresa el número en la posición " + (j + 1) +  ": ");
               var num = entrada.nextInt(); 
               System.out.println();
               
               if ((numeros_al_azar[j]) == num) {
                   System.out.println("¡Excelente!");
                   System.out.println();
                 puntaje++;
               }
               else {
                   System.out.println("Te has equivocado :(");
                   System.out.println();
               }
           }
           
           if (puntaje >= 3) {
               System.out.println("Tu puntaje fue de: " + puntaje);
               System.out.println("¡Felicidades, has ganado!! ");
        } 
           else {
               System.out.println("Tu puntaje fue de: " + puntaje);
               System.out.println("Has perdido :(");
           }
           }   
    }
