package ProyectoFinal;

import java.util.Scanner;

public class PiedraPapelTijera {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String respuesta = "si";

        while (respuesta.equalsIgnoreCase("si")) {
            System.out.println(" ");
            System.out.println("Ronda 1");
            System.out.println("Elije una opción:");
            System.out.println(" ");
            System.out.println("1. para Piedra");
            System.out.println("2. para Papel");
            System.out.println("3. para Tijera");

            int jugadaJugador;
            while (!input.hasNext()) {
                System.out.println("Por favor, elige una opción.");
                input.nextLine();
            }
            jugadaJugador = input.nextInt();
            input.nextLine(); // Limpiar el búfer de entrada

            int jugadaComputadora = (int) (Math.random() * 3) + 1;
            System.out.println(" ");
            System.out.println("Elegiste " + jugadaJugador);
            System.out.println("Jugador elige: " + opcion(jugadaJugador));
            System.out.println("Computadora elige: " + opcion(jugadaComputadora));

            int resultado = comparar(jugadaJugador, jugadaComputadora);
            if (resultado == 0) {
                System.out.println("Empate en esta ronda.");
            } else if (resultado == 1) {
                System.out.println("Jugador gana esta ronda.");
            } else {
                System.out.println("Computadora gana esta ronda.");
            }

            System.out.println(" ");
            System.out.println("Ronda 2");
            System.out.println("Elije una opción:");
            System.out.println(" ");
            System.out.println("1. para Piedra");
            System.out.println("2. para Papel");
            System.out.println("3. para Tijera");

            while (!input.hasNext()) {
                System.out.println("Por favor, elige una opción.");
                input.nextLine();
            }
            jugadaJugador = input.nextInt();
            input.nextLine(); // Limpiar el búfer de entrada

            jugadaComputadora = (int) (Math.random() * 3) + 1;
            System.out.println(" ");
            System.out.println("Elegiste " + jugadaJugador);
            System.out.println("Jugador elige: " + opcion(jugadaJugador));
            System.out.println("Computadora elige: " + opcion(jugadaComputadora));

            resultado = comparar(jugadaJugador, jugadaComputadora);
            if (resultado == 0) {
                System.out.println("Empate en esta ronda.");
            } else if (resultado == 1) {
                System.out.println("Jugador gana esta ronda.");
            } else {
                System.out.println("Computadora gana esta ronda.");
            }

            System.out.println(" ");
            System.out.println("Ronda 3");
            System.out.println("Elije una opción:");
            System.out.println(" ");
            System.out.println("1. para Piedra");
            System.out.println("2. para Papel");
            System.out.println("3. para Tijera");

            while (!input.hasNext()) {
                System.out.println("Por favor, elige una opción.");
                input.nextLine();
            }
            jugadaJugador = input.nextInt();
            input.nextLine(); // Limpiar el búfer de entrada

            jugadaComputadora = (int) (Math.random() * 3) + 1;
            System.out.println(" ");
            System.out.println("Elegiste " + jugadaJugador);
            System.out.println("Jugador elige: " + opcion(jugadaJugador));
            System.out.println("Computadora elige: " + opcion(jugadaComputadora));

            resultado = comparar(jugadaJugador, jugadaComputadora);
            if (resultado == 0) {
                System.out.println("Empate en esta ronda.");
            } else if (resultado == 1) {
                System.out.println("Jugador gana esta ronda.");
            } else {
                System.out.println("Computadora gana esta ronda.");
            }

            System.out.println(" ");
            System.out.println("--- Resultado Final ---");
            int puntosJugador = 0;
            int puntosComputadora = 0;
            if (comparar(jugadaJugador, jugadaComputadora) == 1) {
                puntosJugador++;
            } else if (comparar(jugadaJugador, jugadaComputadora) == -1) {
                puntosComputadora++;
            }
            if (comparar(jugadaJugador, jugadaComputadora) == 1) {
                puntosJugador++;
            } else if (comparar(jugadaJugador, jugadaComputadora) == -1) {
                puntosComputadora++;
            }
            if (comparar(jugadaJugador, jugadaComputadora) == 1) {
                puntosJugador++;
            } else if (comparar(jugadaJugador, jugadaComputadora) == -1) {
                puntosComputadora++;
            }
            System.out.println("Puntos del Jugador: " + puntosJugador);
            System.out.println("Puntos de la Computadora: " + puntosComputadora);
            if (puntosJugador > puntosComputadora) {
                System.out.println("¡Jugador gana el juego!");
            } else if (puntosJugador < puntosComputadora) {
                System.out.println("¡Computadora gana el juego!");
            } else {
                System.out.println("El juego termina en empate.");
            }

            System.out.print("¿Quieres jugar de nuevo? (si o no): ");
            if (input.hasNext()) {
                respuesta = input.next();
            } else {
                respuesta = "";
            }
            System.out.println();
            input.nextLine(); // Limpiar el búfer de entrada después de la respuesta

        }
    }

    public static String opcion(int jugada) {
        String opcion = "";
        switch (jugada) {
            case 1 -> opcion = "Piedra";
            case 2 -> opcion = "Papel";
            case 3 -> opcion = "Tijera";
        }
        return opcion;
    }

    public static int comparar(int jugadaJugador, int jugadaComputadora) {
        if (jugadaJugador == jugadaComputadora) {
            return 0;
        } else if ((jugadaJugador == 1 && jugadaComputadora == 3) || (jugadaJugador == 2 && jugadaComputadora == 1)
                || (jugadaJugador == 3 && jugadaComputadora == 2)) {
            return 1;
        } else {
            return -1;
        }
    }

}

