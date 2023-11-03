package ejerciciociclos10;

import javax.swing.JOptionPane;

public class Ciclos10OptionPane {

    public static void main(String[] args) {
        int número, suma = 0;
        for (int i = 1; i < 10; i++) {
            String input = JOptionPane.showInputDialog("Digite un número:");
            número = Integer.parseInt(input);
            suma += número;
        }
        JOptionPane.showMessageDialog(null, "La suma de todos los números es: " + suma);
    }
}
