 
package ejerciciociclos04;

import java.util.Scanner;


 
public class EjercicioCiclos04 {

    
    public static void main(String[] args) {
       Scanner entrada = new Scanner(System.in);
       int numero,conteo = 0;
        System.out.println("Digite un número:");
        numero = Integer.parseInt(entrada.nextLine()) ;
        while (numero>=0){
            System.out.println("El número: "+ numero + "es positivo");
            conteo++;
            System.out.println("Digite otro numero");
            numero = Integer.parseInt(entrada.nextLine());
            
        }
        System.out.println("A ingresado "+conteo+"Diez numeros que son negativos");
    }
    
}
