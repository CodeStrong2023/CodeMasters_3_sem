/*Leer números hasta que se untroduzca un cero.
Para cado uno indicar si es par o impar.
 */
package Ciclos3;

import javax.swing.JOptionPane;

public class Ejercicio3v2 {
    public static void main(String[] args) {
         var numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        while(numero!=0){
            if(numero % 2 == 0){
                JOptionPane.showMessageDialog(null, "El número "+numero+" es Par.");
            }
            else { 
                 JOptionPane.showMessageDialog(null, "El número "+numero+" es Impar.");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        }
        JOptionPane.showMessageDialog(null, "El número "+numero+" finaliza el programa.");
    }
    
}
