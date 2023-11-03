 
package ejerciciociclos10;

import java.util.Scanner;

public class EjercicioCiclos10 {

    public static void main(String[] args) {
       Scanner entrada = new Scanner(System.in);
       int número, suma = 0;
       for(int i=1; i <10; i++){
           System.out.println("Digiter un número: ");
           número = Integer.parseInt(entrada.nextLine());
           suma += número;
       }
        System.out.println("\nLa suma de todos los numeros es:"+ suma);
    }
    
}
