/*Pedir números hasta que se teclee uno negativo,
y mostrar cuántos números se han introducido. 
 */
package Ciclos4;

import javax.swing.JOptionPane;

public class Ejercicio4v2 {
    public static void main(String[] args) {
         int numero, conteo = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        while (numero >= 0) {
             JOptionPane.showMessageDialog(null, "El número "+numero+" es Positivo.");
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
            
        }
         JOptionPane.showMessageDialog(null, "Se han ingresado "+conteo+" números que no son negativos.");
    }
}
