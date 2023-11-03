package ProyectoFinal;

import java.util.Scanner;

public class Ahorcado {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int x, n, a, error, c;
        char letra;
        String secreta;

        // Solicitar la palabra secreta al usuario
        System.out.println("Ingresa la palabra secreta:");
        secreta = scanner.nextLine();

        // Obtener la longitud de la palabra secreta
        n = secreta.length();

        // Declarar los arrays para almacenar las letras adivinadas
        char[] vector1 = new char[50];
        char[] vector2 = new char[50];

        // Inicializar los arrays con valores iniciales
        for (x = 0; x < n; x++) {
            vector1[x] = secreta.charAt(x);
            vector2[x] = '_';
        }

        // Inicializar contadores
        a = 0;
        c = 0;

        // Iniciar el juego
        while (a < 5) {
            for (x = 0; x < n; x++) {
                System.out.print(vector2[x] + " ");
            }
            System.out.println(); // salto de línea
            System.out.println("Ingresa una letra:");
            letra = scanner.next().charAt(0);
            error = 1; // Indicador de error

            // Comprobar si la letra ingresada está en la palabra secreta
            for (x = 0; x < n; x++) {
                if (letra == vector1[x]) {
                    if (vector2[x] == '_') {
                        vector2[x] = letra; // Actualizar la letra adivinada en vector2
                        error = 0; // Indicar que no hay error
                        c++; // Incrementar el contador de letras correctas
                    }
                }
            }

            // Comprobar si se han adivinado todas las letras
            if (c == n) {
                System.out.println("¡Felicidades! Has ganado el juego.");
                System.out.println("La palabra secreta era: " + secreta);
                a = 6;
            } else {
                if (error == 1) {
                    a++; // Incrementar el contador de intentos fallidos
                }

                // Mostrar el ahorcado según la cantidad de intentos fallidos
                switch (a) {
                    case 1 -> {
                        System.out.println(".");
                        System.out.println(".");
                        System.out.println(".");
                        System.out.println(".");
                        System.out.println("Te quedan 4 intentos.");
                    }
                    case 2 -> {
                        System.out.println(".....");
                        System.out.println(".");
                        System.out.println(".");
                        System.out.println(".");
                        System.out.println("Te quedan 3 intentos.");
                    }
                    case 3 -> {
                        System.out.println(".....");
                        System.out.println(".   o");
                        System.out.println(".");
                        System.out.println(".");
                        System.out.println("Te quedan 2 intentos.");
                    }
                    case 4 -> {
                        System.out.println(".....");
                        System.out.println(".   o");
                        System.out.println(".   ^");
                        System.out.println(".");
                        System.out.println("Te queda 1 intento.");
                    }
                    case 5 -> {
                        System.out.println(".....");
                        System.out.println(".   o");
                        System.out.println(".   ^");
                        System.out.println(".   ^");
                        System.out.println("AHORCADO");
                    }
                }
            }
        }
    }
}
