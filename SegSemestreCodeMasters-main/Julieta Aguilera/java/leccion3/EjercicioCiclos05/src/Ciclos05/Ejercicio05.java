/*
Ejercicio 5: Realizar un juego para adivinar un numero,
para ello generar un numero aleatorio entre 0-100, y
luego ir pidiendo numero indicando "es mayoe" o "es menor"
seun sea mayor o menor con respecto a n
El proceso termina cuando el usuario acierta y mostramos 
el numero de intentos
 */
package Ciclos05;

import javax.swing.JOptionPane;

public class Ejercicio05 {
    public static void main(String[] args) {
       int numero, aleatorio, contador = 0;
        aleatorio = (int)(Math.random()*100); //Esto genera un numero aleatorio
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            if(numero <aleatorio){
                JOptionPane.showMessageDialog(null,"Digite un numero mayor: " );    
            }
            else if(numero > aleatorio){
                JOptionPane.showMessageDialog(null,"Digite un numero menor: " );
            }
            else{
                JOptionPane.showMessageDialog(null,"¡Felicidades! Has adivinado el numero " );
            }
            contador++;   
        }while(numero != aleatorio);
        JOptionPane.showMessageDialog(null,"Adivinaste en "+contador+" intentos" );
    }   
} 
        
     

