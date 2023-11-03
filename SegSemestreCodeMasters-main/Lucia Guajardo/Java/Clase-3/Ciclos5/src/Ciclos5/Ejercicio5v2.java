/*Realizar un juego para adivinar un número, para ello generar un número aleatorio entre
0-100, y luego ir pidiendo números indicando "es mayor" o "es menor" según sea mayoe
o menor con respecto a N. El proceso termina cuando el usuario acierta y mostarmos el número
de intentos hechos.
 */
package Ciclos5;

import javax.swing.JOptionPane;

public class Ejercicio5v2 {
    public static void main(String[] args) {
         int numero, aleatorio, conteo = 0;
        aleatorio = (int) (Math.random()*100);
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
            if(numero < aleatorio) {
                 JOptionPane.showMessageDialog(null, "Ingrese un número mayor:");
            }
            else if(numero > aleatorio){
                 JOptionPane.showMessageDialog(null, "Ingrese un número menor:");
            }
            else{
                 JOptionPane.showMessageDialog(null, "¡Felicidades, has adivinado el número!");
            }
            conteo++;
        }while (numero != aleatorio);
         JOptionPane.showMessageDialog(null, "Adivinaste en: "+conteo+" intentos.");
    }
    
}
