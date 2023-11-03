/*Pedir un número y calcular su factorial.
 */
package ciclos12;

import javax.swing.JOptionPane;

public class Ejercicio12v2 {
    public static void main(String[] args) {
         long factorial = 1;
         int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
         for (int i=1; i<=numero; i++) {
             factorial *=i;
         }
           JOptionPane.showMessageDialog(null, "El factorial del número ingresado es: "+factorial);
    }
    
}
