/*
Ejercicio 3: Leer números hasta que se introduzca un cero.
Para cada uno indicar si es par o impara.
Primero lo haremos con la clase scanner
Luego con la clase JOptionPane
 */
package Ciclos03;

import javax.swing.JOptionPane;

public class Ejercicio03 {

    public static void main(String[] args) {

        int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        while (numero != 0) {
            if (numero % 2 == 0) {
                System.out.println("El número ingresado " + numero + " es PAR");

            } else {
                System.out.println("El número ingresado " + numero + " es IMPAR");
            }
            System.out.println("Dijite otro número: ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Introduzca otro número: "));
        }
        System.out.println("El número ingresado es " + numero + " finaliza el programa");
    }

}
