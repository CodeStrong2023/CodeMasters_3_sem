package ProyectoFinal;

import java.util.Scanner;

public class AdivinaLaPalabra {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        String palabra, palabra2, pista;

        System.out.println("Bienvenido a Adivina la palabra");
        System.out.println("Aclaración: La palabra que elijas debes escribirla con la inicial en mayúscula y con su respectivo tilde si lo requiere.");
        System.out.println("Ingrese la palabra que el otro usuario adivine: ");
        palabra = entrada.nextLine();
        System.out.println("Ingrese la pista: ");
        pista = entrada.nextLine();

        System.out.println("\n\n\n\n\n\n\n");
        System.out.println("La pista es: " + pista);

        System.out.println("A continuación ingrese la palabra: ");
        palabra2 = entrada.nextLine();

        if (palabra2.equals(palabra)) {
            // Si la palabra ingresada es correcta se ejecutará lo siguiente:
            System.out.println("¡FELICIDADES, GANASTE!");
        } else {
            System.out.println("PERDISTE");
        }
    }
}
