/*Pedir el día, mes y año de una fecha e indicar
si la fecha es correcta,Suponiendo que todos los meses 
son de 30 días.
 */
package Ciclos9;

import javax.swing.JOptionPane;

public class Ejercicio9v2 {
    public static void main(String[] args) {
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número de día: "));
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número de mes: "));
        int anio = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un año: "));
        if((dia != 0)&&(dia <= 30)) {
            if((mes != 0)&&(mes <= 12)) {
                if ((anio != 0)&&(anio <= 2022)) {
                    JOptionPane.showMessageDialog(null, "La fecha ingresada es: "+dia+"/"+mes+"/"+anio);
                }
                else {
                    JOptionPane.showMessageDialog(null,"Año incorrecto.");
                }
            }
            else {
                JOptionPane.showMessageDialog(null,"Mes incorrecto.");
            }
        }
        else {
            JOptionPane.showMessageDialog(null,"Fecha incorrecta.");
        }
    }
}
