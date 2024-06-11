import java.util.Scanner;

public class CalculadoraUTN {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        System.out.println("***** Aplicación Calculadora *****");
        // MENÚ:
        System.out.println("""
                1) Suma
                2) Resta
                3) Multiplicación
                4) División
                5) Salir
                """);

        System.out.print("Que desea realizar? ");
        var operacion = Integer.parseInt(entrada.nextLine());

        if(operacion  >= 1 && operacion <= 4){
            System.out.print("Digite el valor para el operando 1: ");
            var operando1 = Integer.parseInt(entrada.nextLine());
            System.out.print("Digite el valor para el operando 2: ");
            var operando2 = Integer.parseInt(entrada.nextLine());

            int resultado;
            switch (operacion){
                //SUMA
                case 1 -> {
                    resultado = operando1 + operando2;
                    System.out.println("Resultado de la suma: "+resultado);
                }
                //RESTA
                case 2 -> {
                    resultado = operando1 - operando2;
                    System.out.println("Resultado de la resta: "+resultado);
                }
                //MULTIPLICACION
                case 3 ->{
                    resultado = operando1 * operando2;
                    System.out.println("Resultado de la multiplicación: "+resultado);
                }
                //DIVISION
                case 4 -> {
                    resultado = operando1 / operando2;
                    System.out.println("Resultado de la división: "+resultado);
                }
                default -> System.out.println("Opción invalida: "+operacion);
            } // FIN SWITCH

        } // FIN DEL IF
        else if (operacion == 5) {
            System.out.println("Has seleccionado salir. Hasta pronto..");
        }
        else {
            System.out.println("Operacion error: "+operacion);
        }

    } // FIN MAIN
} // FIN CLASE
