package ProyectoFinal;

import java.util.Scanner;

public class Tateti {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int opcion;
        String tablero[][] = new String[3][3];

        for (int f = 0; f < 3; f++) {
            for (int c = 0; c < 3; c++) {
                tablero[f][c] = " ";
            }
        }

        System.out.println("BIENVENIDO A Ta-Te-Ti");
        System.out.println("Presione 1 para empezar el juego");
        opcion = entrada.nextInt();

        int jugActual = 1;
        String simJug = "X";
        int finJuego = 0;
        int empate = 0;

        if (opcion == 1) {
            do {
                // Mostrar el tablero actual
                System.out.println("             1   2   3");
                System.out.println("           *-----------*");
                for (int f = 0; f < 3; f++) {
                    System.out.print("         " + (f + 1) + " | ");
                    for (int c = 0; c < 3; c++) {
                        System.out.print(tablero[f][c] + " | ");
                    }
                    System.out.println("\n           |---+---+---|");
                }
                System.out.println("           *-----------*");

                // Solicitar la jugada al jugador
                int fila, columna;
                do {
                    System.out.print("Jugador " + jugActual + " (" + simJug + "), ingresa la fila (1-3): ");
                    fila = entrada.nextInt() - 1;
                    System.out.print("Jugador " + jugActual + " (" + simJug + "), ingresa la columna (1-3): ");
                    columna = entrada.nextInt() - 1;
                } while (fila < 0 || fila > 2 || columna < 0 || columna > 2 || !tablero[fila][columna].equals(" "));

                // Marcar la casilla con la jugada del jugador
                tablero[fila][columna] = simJug;

                // Verificar si hay un ganador
                finJuego++;
                if (tablero[0][0].equals(simJug) && tablero[0][1].equals(simJug) && tablero[0][2].equals(simJug)
                        || tablero[1][0].equals(simJug) && tablero[1][1].equals(simJug) && tablero[1][2].equals(simJug)
                        || tablero[2][0].equals(simJug) && tablero[2][1].equals(simJug) && tablero[2][2].equals(simJug)
                        || tablero[0][0].equals(simJug) && tablero[1][0].equals(simJug) && tablero[2][0].equals(simJug)
                        || tablero[0][1].equals(simJug) && tablero[1][1].equals(simJug) && tablero[2][1].equals(simJug)
                        || tablero[0][2].equals(simJug) && tablero[1][2].equals(simJug) && tablero[2][2].equals(simJug)
                        || tablero[0][0].equals(simJug) && tablero[1][1].equals(simJug) && tablero[2][2].equals(simJug)
                        || tablero[0][2].equals(simJug) && tablero[1][1].equals(simJug) && tablero[2][0].equals(simJug)) {
                    System.out.println("¡Jugador " + jugActual + " (" + simJug + ") gana!");
                    break;
                }

                // Cambiar de jugador
                jugActual = (jugActual % 2) + 1;
                simJug = (jugActual == 1) ? "X" : "O";

                // Verificar empate
                empate++;
                if (empate == 9) {
                    System.out.println("¡Empate!");
                    break;
                }
            } while (finJuego < 9);
        }
    }
}
