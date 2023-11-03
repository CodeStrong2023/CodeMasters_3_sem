
package Ciclos07;

import java.util.Scanner;

public class Ciclos07 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0, suma = 0;
        float media = 0;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0){
            conteo += numero;
            suma += 1;
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        media = conteo / suma;
        System.out.println("El promedio de los numeros ingresados es: "+media);
    }
}
