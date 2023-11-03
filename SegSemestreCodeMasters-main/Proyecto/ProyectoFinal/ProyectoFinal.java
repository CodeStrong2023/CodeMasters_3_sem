package ProyectoFinal;

import java.util.Scanner;

public class ProyectoFinal {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String respuesta;

        do {
            System.out.println("*-------------------------------------------------------------------------------------------------------------*");
            System.out.println("*                                                                                                             *");
            System.out.println("*                                      BIENVENIDO A RETOS GAMES                                               *");
            System.out.println("*                                                                                                             *");
            System.out.println("*                    ESTE JUEGO TIENE UN CATÁLOGO PARA QUE PUEDAS ELEGIR EL QUE MÁS TE GUSTE                    *");
            System.out.println("*-------------------------------------------------------------------------------------------------------------*");
            System.out.println();

            System.out.println("  Menú de juegos:");
            System.out.println();
            System.out.println(" (1) opción 1: Piedra, Papel o Tijera");
            System.out.println(" (2) Opción 2: Tateti");
            System.out.println(" (3) Opción 3: Ahorcado");
            System.out.println(" (4) Opción 4: Adivina palabra");
            System.out.println(" (5) Opción 5: Memoria");
            System.out.print("Selecciona un número del 1 al 5 para jugar los siguientes juegos: ");
            int opc = input.nextInt();

            switch (opc) {
                case 1:
                    PiedraPapelTijera.main(null); // Llamar al juego Piedra, Papel o Tijera
                    break;
                case 2:
                    // Llamar al juego Tateti
                    break;
                case 3:
                    // Llamar al juego Ahorcado
                    break;
                case 4:
                    // Llamar al juego Adivina la Palabra
                    break;
                case 5:
                    // Llamar al juego Memoria
                    break;
                default:
                    System.out.println("Opción no válida.");
            }

            System.out.println();
            System.out.print("¿Quieres jugar otro juego? (si o no): ");
            respuesta = input.next();
            System.out.println();
        } while (respuesta.equalsIgnoreCase("si"));

        System.out.println("JUEGO FINALIZADO... ¡Gracias por jugar Reto Games y esperamos volver a verte!");
        System.out.println();
        System.out.println("Integrantes del grupo: ");
        System.out.println();
        System.out.println("Aguilera Erica Julieta");
        System.out.println("Bala Ignacio");
        System.out.println("Carreras Castellano Virginia");
        System.out.println("Castro Luciana");
        System.out.println("Cirica Mateo");
        System.out.println("Guajardo Lucia");
        System.out.println("Houlne Alejo");
        System.out.println("Mercatante Augusto");
        System.out.println("Rodriguez Maricel Romina");
    }
}
