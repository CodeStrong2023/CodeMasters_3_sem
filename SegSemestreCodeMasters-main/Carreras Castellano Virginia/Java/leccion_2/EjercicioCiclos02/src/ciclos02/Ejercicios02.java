/*
 leer un número digitar si es positivo o negativo 
 */
package ciclos02;

import java.util.Scanner;

public class Ejercicios02 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("digite un número");
        var numero = Integer.parseInt(entrada.nextLine());
        while (numero != 0) {
            if (numero > 0) {
                System.out.println("el número " + numero + " es POSITIVO ");
            }
            else{
                System.out.println("el número " + numero + " es NEGATIVO ");
            }
            System.out.println("Digite otro numero");
            numero=Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El número "+numero+ " finaliza el programa ");
    }
}
