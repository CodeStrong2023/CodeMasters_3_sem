package ciclos01;

import javax.swing.JOptionPane;

//leer un númer y mostrar su cuadrado, repetir el proceso hasta que se digite un número negativo
public class ejercicio01 {

    public static void main(String[] args) {
        int numero, cuadrado;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número"));
        while (numero
                >= 0) {  //mientra el número sea igual a cero o positivo
            cuadrado = (int) Math.pow(numero, 2);
            System.out.println("el número " + numero + " elevado al cuadrado: " + cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número"));

        }
        System.out.println("el programa a finalizado por números negativos");
    }

}
