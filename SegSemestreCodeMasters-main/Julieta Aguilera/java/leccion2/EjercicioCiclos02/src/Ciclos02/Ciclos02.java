/*
Ejercicio 2: Leer un numero e indicar si es positivo o
negativo. El proceso se repetira hasta que se introduzca
un cero 0
Hacer ese ejercicio con la clase Scanner,
luego hacerlo con la clase JOptionpane

*/
package Ciclos02;
import javax.swing.JOptionPane;
public class Ciclos02 {
    public static void main(String[] args) {
        var numero = Integer.parseInt(JOptionPane.showInputDialog("DIgite un numero: "));
        while(numero != 0) {
            if(numero > 0){
             JOptionPane.showMessageDialog(null, "El numero "+numero+ " es Positivo");   
            }
            else{
                JOptionPane.showMessageDialog(null, "El numero "+numero+ " es Negativo");
            }
            
            numero = Integer.parseInt(JOptionPane.showInputDialog("DIgite otro numero: "));
        }
        JOptionPane.showMessageDialog(null, "El numero "+numero+ " finaliza el programa");
                
    }
}
