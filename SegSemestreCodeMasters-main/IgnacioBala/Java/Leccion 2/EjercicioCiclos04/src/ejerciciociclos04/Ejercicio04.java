
package ejerciciociclos04;

import javax.swing.JOptionPane;


public class Ejercicio04 {
    public static void main(String[] args) {
         int numero,conteo = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número:")) ;
        while (numero>=0){
            JOptionPane.showMessageDialog(null, "El número: "+ numero + " es positivo");
            conteo++;
             numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número:")) ;
            
        }
         JOptionPane.showMessageDialog(null, "A ingresado "+conteo+"Diez numeros que son negativos");
    
        
    }
 
}
