/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Clases;

/**
 *
 * @author Usuario
 */
public class PruebaPersona {
   


    public static void main(String[] args) {
        Persona persona1; 
        persona1 = new Persona(); //LLamamos al constructor 
        persona1.nombre = "Ignacio";
        persona1.apellido = "Bala";
        persona1.obtenerInformacion();
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        persona2.obtenerInformacion();
        persona2.nombre = "Daniel";
        persona2.apellido = "Barbosa";
                
               
}
}
