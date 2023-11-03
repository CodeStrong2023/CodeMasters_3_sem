/*Leer un número e indicar si es positivo o negativo.
El proceso se repetira hasta que se introduzca un cero.
 */
package Ciclos2;

import javax.swing.JOptionPane;

public class Ejercicio2v2 {
    public static void main(String[] args) {
         var numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        while(numero!=0){
            if(numero > 0){
                JOptionPane.showMessageDialog(null, "El número "+numero+" es Positivo.");
            }
            else { 
                 JOptionPane.showMessageDialog(null, "El número "+numero+" es Negativo.");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        }
        JOptionPane.showMessageDialog(null, "El número "+numero+" finaliza el programa.");
    }
}
