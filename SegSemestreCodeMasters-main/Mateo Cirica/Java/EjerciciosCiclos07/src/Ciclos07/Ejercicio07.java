package Ciclos07;

import javax.swing.JOptionPane;

public class Ejercicio07 {
    public static void main(String[] args) {
        int numero, conteo = 0, suma = 0;
        float media = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero >= 0){
            conteo += numero;
            suma += 1;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        media = conteo / suma;
        JOptionPane.showMessageDialog(null, "El promedio de los numeros ingresados es: "+media);
    }
}
