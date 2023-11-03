/*
Ejercicio 9: Pedir el dia, mes y año de una fecha 
e indicar si la fecha es corecta. Suponiendo que 
todos los meses son de 30 días
*/
package Ciclo09;

import javax.swing.JOptionPane;


public class Ejercicio09 {
    public static void main(String[] args) {
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Digite un día: "));
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Digite un mes: "));
        int año = Integer.parseInt(JOptionPane.showInputDialog("Digite un año: "));
         if((dia != 0)&&(dia <= 30)){
            if((mes != 0)&&(mes <= 12)){
                if((año != 0)&&(año <= 2022)){
                    JOptionPane.showInputDialog("La fecha ingresada es: "+dia+"/"+mes+"/"+año);
                }
                else{
                    JOptionPane.showInputDialog("Fecha incorrecta, año incorrectos");
                }
            }    
            else{
                  JOptionPane.showInputDialog("Fecha incorrecta, mes incorrecto");
                }
        }    
        else{
            JOptionPane.showInputDialog("Fecha incorecta, dia incorrecto");
        }
    }
}
