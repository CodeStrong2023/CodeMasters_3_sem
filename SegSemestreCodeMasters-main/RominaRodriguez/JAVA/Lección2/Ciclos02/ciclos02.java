/*
Ejercicio 2: Leer un número e indecar si es positivo
o negativo.El proceso se repetira hasta que se ingrese 
un cero 0
Hacer este ejercicio con la clase scanner y luego con la 
clase JOptionPane
 */
package Ciclos02;

import javax.swing.JOptionPane;

public class ciclos02 {

    public static void main(String[] args) {
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while (numero != 0) {
            if (numero > 0) {
                System.out.println("El número " + numero + " es POSITIVO");
            } else {
                System.out.println("El número " + numero + " es NEGATIVO");

            }
            System.out.println("Digite otro número: ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));

        }
        System.out.println("El número " + numero + " finaliza el programa");
    }
}
