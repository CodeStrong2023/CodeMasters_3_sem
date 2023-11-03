
package juego;

import java.util.Scanner;

public class AdivinaLaPalabra {
    public static void main(String[] args){
    Scanner scanner = new Scanner(System.in);
    
    String palabra, palabra2, pista;
    System.out.println("Bienvenido a Adivina la palabra"); 
    System.out.println("Aclaracion: La palabra que elijas debes escribirla con la inicial en mayúscula y con su respectivo tilde si lo requiere.");
    System.out.println("Ingrese la palabra que el otro usuario adivinará: ");
    palabra = scanner.nextLine();
    System.out.println("Ingrese la pista: ");
    pista = scanner.nextLine();
    
    System.out.println("\n\n\n\n\n\n\n");
    System.out.println("La pista es: "+pista);
    
    System.out.println("A continuacion ingrese la palabra: ");
    palabra2 = scanner.nextLine();
    
    if(palabra2.equals(palabra)){
        //Si la palabra ingresada es correcta se ejecutara lo siguiente:
        System.out.println("Â¡FELICIDADES, GANASTE!");
    }
    else{
        System.out.println("PERDISTE");
    }
    
    }
}
