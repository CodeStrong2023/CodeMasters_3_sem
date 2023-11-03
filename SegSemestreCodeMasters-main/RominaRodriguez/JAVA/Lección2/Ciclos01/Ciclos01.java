/*
Ejercicio 1: Leer un numero y mostrar su cuadrado,
repetir el procesos hasta que se introduzca un número
negativo
*/
package ciclos01;

import java.util.Scanner;


public class Ciclos01 {
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        int numero , cuadrado;
        System.out.println("Digite un  numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0){
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El número "+numero+" elevado al cuadrado es: "+cuadrado);
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El programa a finalizado por número negativo"); 
    }
        
    
}
