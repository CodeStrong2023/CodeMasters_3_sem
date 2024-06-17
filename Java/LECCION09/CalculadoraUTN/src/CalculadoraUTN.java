import java.util.Scanner;

public class CalculadoraUTN {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        System.out.println("***** Aplicación Calculadora *****");
        mostrarMenu();

            while(true) {//Ciclo infinite


        try {
            var operacion = Integer.parseInt(entrada.nextLine());

            if (operacion >= 1 && operacion <= 4) {

                ejecutarOperacion(operacion, entrada);


            } // FIN DEL IF
            else if (operacion == 5) {
                System.out.println("Has seleccionado salir. Hasta pronto..");
                break;
            } else {
                System.out.println("Operacion error: " + operacion);
            }
            //Imprimimos un salto de linea antes de reptir menu
            System.out.println();
        } catch (Exception e){//Fin del try comiwnzo catch
            System.out.println();
            System.out.println("Ocurrió un error: "+e.getMessage());
        }
                }// Fin whilw
    } // FIN MAIN

    private static void mostrarMenu(){
        // MENÚ:
        System.out.println("""
                1) Suma
                2) Resta
                3) Multiplicación
                4) División
                5) Salir
                """);

        System.out.print("Que desea realizar? ");

    }//Fin metodo mostrar menu
    private static void ejecutarOperacion(int operacion, Scanner entrada){
        System.out.print("Digite el valor para el operando 1: ");
        var operando1 = Double.parseDouble(entrada.nextLine());
        System.out.print("Digite el valor para el operando 2: ");
        var operando2 = Double.parseDouble(entrada.nextLine());
        Double resultado;
        switch (operacion) {
            //SUMA
            case 1 -> {
                resultado = operando1 + operando2;
                System.out.println("Resultado de la suma: " + resultado);
            }
            //RESTA
            case 2 -> {
                resultado = operando1 - operando2;
                System.out.println("Resultado de la resta: " + resultado);
            }
            //MULTIPLICACION
            case 3 -> {
                resultado = operando1 * operando2;
                System.out.println("Resultado de la multiplicación: " + resultado);
            }
            //DIVISION
            case 4 -> {
                resultado = operando1 / operando2;
                System.out.println("Resultado de la división: " + resultado);
            }
            default -> System.out.println("Opción invalida: " + operacion);
        } // FIN SWITCH
    }//Fin metodo ejecutar operacion
} // FIN CLASE
