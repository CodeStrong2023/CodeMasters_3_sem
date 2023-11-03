package ciclos01;

import java.util.Scanner;
//leer un númer y mostrar su cuadrado, repetir el proceso hasta que se digite un número negativo 
public class Ciclos01 {

    public static void main(String[] args) {
        Scanner entrada= new  Scanner(System.in);
        int numero, cuadrado;
        System.out.println("Digite un número: ");
        numero= Integer.parseInt(entrada.nextLine());
        while(numero>=0){  //mientra el número sea igual a cero o positivo
            cuadrado= (int)Math.pow(numero, 2);
            System.out.println("el número"+ numero +"elevado al cuadrado: "+ cuadrado );
            System.out.println("Digite otro número: ");
            numero= Integer.parseInt(entrada.nextLine());
            
        } 
        System.out.println("el programa a finalizado por números negativos");
    }

}
