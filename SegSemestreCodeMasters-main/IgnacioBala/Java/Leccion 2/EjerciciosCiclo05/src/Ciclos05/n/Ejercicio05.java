    
package Ciclos05.n;

import javax.swing.JOptionPane;

/**
 *
 * @author Usuario
 */
public class Ejercicio05 {
    public static void main(String[] args) {
         int numero,aleatorio, conteo = 0 ;
        aleatorio = (int)(Math.random()*100); //Estop genera un número aleatorio
        do{
            
         
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número:"));
            
            if(numero<aleatorio){
               JOptionPane.showMessageDialog( null, "Digite un número mayor ");
                
            }
            else if(numero>aleatorio){
                  JOptionPane.showMessageDialog( null, "Digite un número menor ");
            }
            else{
                JOptionPane.showMessageDialog(null, "Felicidades has adivinado el numero");
                
            }
            conteo++ ;
            
        }while(numero!=aleatorio);
        JOptionPane.showMessageDialog(null, "Adivinaste el número en : " +conteo+ "intentos");
    }
}
