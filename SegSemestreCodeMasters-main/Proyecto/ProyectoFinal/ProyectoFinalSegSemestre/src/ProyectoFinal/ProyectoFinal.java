package ProyectoFinal;

import java.util.Scanner;

public class ProyectoFinal {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String respuesta = "si"; // Inicializamos la respuesta con "si" para que entre al bucle.

        do {
            // Mensaje de bienvenida y presentación del menú.
            System.out.println("*-------------------------------------------------------------------------------------------------------------*");
            System.out.println("*                                                                                                             *");
            System.out.println("*                                      BIENVENIDO A RETOS GAMES                                               *");
            System.out.println("*                                                                                                             *");
            System.out.println("*                    ESTE JUEGO TIENE UN CATÁLOGO PARA QUE PUEDAS ELEGIR EL QUE MÁS TE GUSTE                    *");
            System.out.println("*-------------------------------------------------------------------------------------------------------------*");
            System.out.println();

            System.out.println("  Menú de juegos:");
            System.out.println();
            System.out.println(" (1) Piedra, Papel o Tijera");
            System.out.println(" (2) Tateti");
            System.out.println(" (3) Ahorcado");
            System.out.println(" (4) Adivina palabra");
            System.out.println(" (5) Memoria");
            System.out.print("Selecciona un número del 1 al 5 para jugar los siguientes juegos: ");
            int opc = input.nextInt();
            input.nextLine(); // Limpiar el búfer de entrada después de leer un número.
            
            
            switch (opc) {
                case 1 -> PiedraPapelTijera.main(null); // Llama al juego Piedra, Papel o Tijera
                case 2 -> Tateti.main(null); // Llama al juego Tateti
                case 3 -> Ahorcado.main(null); // Llama al juego Ahorcado
                case 4 -> AdivinaLaPalabra.main(null); // Llama al juego Adivina la Palabra
                case 5 -> JuegoMemoria.main(null); // Llama al juego Memoria
                default -> System.out.println("Opción no válida.");
            }

            System.out.print("¿Quieres jugar otro juego? (si o no): ");
            if (input.hasNext()) {
                respuesta = input.next(); // Lee la respuesta del usuario
            } else {
                respuesta = ""; // Si no hay respuesta, se inicializa como cadena vacía
            }
            System.out.println();
            input.nextLine(); // Limpiar el búfer de entrada después de la respuesta

        } while (respuesta.equalsIgnoreCase("si")); // Continúa si la respuesta es "si"

        // Mensaje de despedida y lista de integrantes del grupo.
        System.out.println("JUEGO FINALIZADO... ¡Gracias por jugar Reto Games y esperamos volver a verte!");
        System.out.println();
        System.out.println("Integrantes del grupo:");
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
