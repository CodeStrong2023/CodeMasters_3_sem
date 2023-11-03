/*
Ejercicio 1: Leer un numero y mostrar su cuadrado,
repetir el procesos hasta que se introduzca un número
negativo
*/
package ciclos01;

import javax.swing.JOptionPane;


public class ejercicio01 {
    public static void main(String[] args) {
         int numero , cuadrado;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(numero >= 0){
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El número "+numero+" elevado al cuadrado es: "+cuadrado);
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        }
        System.out.println("El programa a finalizado por número negativo"); 
    }
    
}
