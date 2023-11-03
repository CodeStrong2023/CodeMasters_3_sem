package PiedraPapelYTijera;

import java.util.Random;
import java.util.Scanner;

public class PiedraPapelYTijera {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        Random random = new Random();
        int jugador, computadora, opcion, resultado;
        String opcion1 = "Piedra";
        String opcion2 = "Papel";
        String opcion3 = "Tijera";
        

        System.out.println("Bienvenidos al Juego de Piedra, Papel y Tijera");
        System.out.println(" ");
  
        for (int ronda =1; ronda <=3; ronda++){
            System.out.println("\nRonda"+ronda);
            System.out.println("Elije una opción");
            System.out.println(" ");
            System.out.println("1. para Piedra");
            System.out.println("2. para Papel");
            System.out.println("3. para Tijera");
            jugador = Integer.parseInt(entrada.nextLine());
            System.out.println("");
        
       
            
            if (jugador == 1) {
                System.out.println("Elegiste " + jugador + " es Piedra");
            }else if (jugador == 2) {
                System.out.println("Elegiste " + jugador + " es Papel");
            } else if(jugador == 3){
                System.out.println("Elegiste " + jugador + " es Tijera");
            } else {
                System.out.println("Opción no válida");
            }              
            computadora = random.nextInt(3) + 1;
            if(computadora == 1){
                System.out.println("La computadora eligió: "+computadora+ " es Piedra");
            }else if (computadora == 2){
                System.out.println("La computadora eligió: "+computadora+ " es Papel");
            }else if (computadora == 3){
                System.out.println("La computadora eligió: "+computadora+ " es Tijera");
            }else {
                System.out.println("Opción no válida");
            }
            
            if(jugador == computadora){
                System.out.println("ES UN EMPATE");
            }else if (jugador==1 & computadora ==2){
                System.out.println("Computadora GANA");
                System.out.println("Jugador PIERDE");
            }else if (jugador ==2 & computadora ==3){
                System.out.println("Computadora GANA");
                System.out.println("Jugador PIERDE");
            }else if (jugador == 3 & computadora == 1){
                System.out.println("Computadora GANA");
                System.out.println("Jugador PIERDE");
            }else if (jugador == 1 & computadora ==3){
                System.out.println("Jugador GANA");
                System.out.println("Computadora PIERDE");
            }else if (jugador ==3 & computadora ==2){
                System.out.println("Jugador GANA");
                System.out.println("Computadora PIERDE");
            }else if (jugador ==2 & computadora ==1){
                System.out.println("Jugador GANA");
                System.out.println("Computadora PIERDE");
            }else {
                System.out.println("Opción Incorrecta, fin del juego");
            }
            System.out.println();
    }    
    entrada.close();
    }
}
