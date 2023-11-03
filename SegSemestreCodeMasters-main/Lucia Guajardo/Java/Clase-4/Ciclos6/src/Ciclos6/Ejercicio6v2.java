/*Pedir numeros hasta que se teclee un 0,
mostrar la suma de todo los números introducidos.
 */
package Ciclos6;

import javax.swing.JOptionPane;

public class Ejercicio6v2 {
    public static void main(String[] args) {
         int numero, suma = 0;
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
            suma+= numero;
        }while(numero != 0);
         JOptionPane.showMessageDialog(null, "La suma de los números ingresados es: "+suma);
    }
}
