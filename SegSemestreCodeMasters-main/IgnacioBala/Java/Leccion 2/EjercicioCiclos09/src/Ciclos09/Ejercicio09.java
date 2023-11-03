/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ciclos09;

import javax.swing.JOptionPane;

/**
 *
 * @author Usuario
 */
public class Ejercicio09 {
    public static void main(String[] args) {
        
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Digite el día"));
        
         int mes = Integer.parseInt(JOptionPane.showInputDialog("Digite el mes"));
       int anio = Integer.parseInt(JOptionPane.showInputDialog("Digite el anio"));
       
        
        if((dia !=0)&&(dia<=30)){
            if((mes!=0)&&(mes<=12)){
                if((anio!=0)&&(anio<=2023)){
                    JOptionPane.showMessageDialog(null, "\"+mes+"+"La fecha ingresada es: "+dia+"/"+mes+"/"+anio);
                }
                else{
                   JOptionPane.showMessageDialog(null, "Fecha Incorrecta año incorrecto");
                }
                
            }
            else{
                 JOptionPane.showMessageDialog(null, "Fecha Incorrecta mes incorrecto");
                          }
        }
        else{
            JOptionPane.showMessageDialog(null, "Fecha Incorrecta dia incorrecto");
    }
    }
   
}
