
package Tateti;

import java.util.Scanner;

public class Tateti {
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        int opcion;
        String tablero [][] = new String [3][3];

        for (int f = 0; f<3; f++){
            for (int c = 0; c<3; c++){
                tablero [f][c] = " ";
            }
        }

        System.out.println("BIENVENIDO A Ta-Te-Ti");
        System.out.println("Presione 1 para empezar el juego");
        opcion = entrada.nextInt();

        int jugActual = 1;
        String simJug = "X";
        int finJuego = 91218;
        int empate = 0;
        String noHuboGanador = "no";

        if (opcion == 1){
            System.out.println("             1   2   3");
            System.out.println("           *-----------*");
            System.out.println("         1 |"+" "+tablero[0][0]+" | "+tablero[0][1]+" | "+tablero[0][2]+" | ");
            System.out.println("           |---+---+---|");
            System.out.println("         2 |"+" "+tablero[1][0]+" | "+tablero[1][1]+" | "+tablero[1][2]+" | ");
            System.out.println("           |---+---+---|");
            System.out.println("         3 |"+" "+tablero[2][0]+" | "+tablero[2][1]+" | "+tablero[2][2]+" | ");
            System.out.println("           *-----------*");

            do{
            
            }while(finJuego == 912);
        }
    }
}
