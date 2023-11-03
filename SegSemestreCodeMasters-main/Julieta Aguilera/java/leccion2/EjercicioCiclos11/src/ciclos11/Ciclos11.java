/*
Ejercicio 11: Diseñar un programa que muestre el prroducto
de los 10 primeros numeros impares
hacerlo con JOptionPane
 */
package ciclos11;

import javax.swing.JOptionPane;

public class Ciclos11 {
    public static void main(String[] args) {
        long producto = 1;
        for(int i = 1; 20>i;i+=2){//El aumento solo apunta a ir a los impares
            producto*= i;
        JOptionPane.showMessageDialog(null,"El producto de los numeros impares es: "+producto );
        
        }
    }
}
