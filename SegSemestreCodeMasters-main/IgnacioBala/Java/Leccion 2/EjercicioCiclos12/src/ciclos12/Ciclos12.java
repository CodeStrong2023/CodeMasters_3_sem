
package ciclos12;

import javax.swing.JOptionPane;


public class Ciclos12 {
    public static void main(String[] args) {
        //Scanner entrada = new Scanner(System.in);
        long factorial = 1;
        //System.out.printIn("Digite un número:");
        int número = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        
        for(int i =1; i<=número ; i++){
            factorial *= i;
        }
          JOptionPane.showMessageDialog(null, "El factorial del numero ingresado es: " +factorial);
            
        }
    
}
