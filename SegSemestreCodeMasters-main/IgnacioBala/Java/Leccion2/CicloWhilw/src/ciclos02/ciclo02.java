package ciclos02;

import java.util.Scanner;



public class ciclo02 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
           System.out.println("Digite un númereo ");
           numero = Integer.parseInt(entrada.nextLine() );
           while(numero !=0){
                if(numero %2 == 0){
                    
                System.out.println("el número ingresado " + numero + " es par");
                }
           
           else{
                   System.out.println("el numero ingresado  = " + numero+"es impar" );
                   
            }
                System.out.println("Digite otro numero");
                Integer.parseInt(entrada.nextLine());
           
           }
           System.out.println("El número ingresado es "+numero+"Finaliza el programa");
    }
}
            