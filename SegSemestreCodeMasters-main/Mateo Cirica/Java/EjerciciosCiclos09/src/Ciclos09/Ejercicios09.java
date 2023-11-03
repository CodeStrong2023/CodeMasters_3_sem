package Ciclos09;

import javax.swing.JOptionPane;

public class Ejercicios09 {
    public static void main(String[] args) {
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Digite el dia: "));
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Digite el mes: "));
        int anio = Integer.parseInt(JOptionPane.showInputDialog("Digite el año: "));
        if((dia !=0) && (dia <= 30)){
            if ((mes != 0) && (mes <= 12)){
                if ((anio != 0) && (anio <= 2023)){
                JOptionPane.showMessageDialog(null, "La fecha ingresada es: "+dia+"/"+mes+"/"+anio);
            }
                else{
                JOptionPane.showMessageDialog(null, "La fecha ingresada es incorrecta");
            }
        }
    }  
    }
}
