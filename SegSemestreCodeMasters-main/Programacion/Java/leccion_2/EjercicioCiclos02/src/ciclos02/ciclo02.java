/*
 leer un número digitar si es positivo o negativo 
 */
package ciclos02;

import javax.swing.JOptionPane;

public class ciclo02 {

    public static void main(String[] args) {
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while (numero != 0) {
            if (numero > 0) {
                System.out.println("el número " + numero + " es POSITIVO ");
            } else {
                System.out.println("el número " + numero + " es NEGATIVO ");
            }
            System.out.println("Digite otro numero");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        }
        System.out.println("El número " + numero + " finaliza el programa ");
    }
}
