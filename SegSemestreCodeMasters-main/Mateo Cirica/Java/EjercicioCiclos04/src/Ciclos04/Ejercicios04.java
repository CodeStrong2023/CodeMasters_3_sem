package Ciclos04;

import javax.swing.JOptionPane;

public class Ejercicios04 {
    public static void main(String[] args) {
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero >= 0){
            JOptionPane.showMessageDialog(null, "El numero ingresado es: "+numero);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        JOptionPane.showMessageDialog(null, "El numero ingresado ("+numero+") finaliza el programa");
    }
}
