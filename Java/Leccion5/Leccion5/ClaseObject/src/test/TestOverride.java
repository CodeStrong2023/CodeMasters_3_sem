/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package test;

import domain.Empleado;
import domain.Persona;
/**
 *
 * @author virginia
 */
public class TestOverride {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Angel", 'M', true);
        Empleado empleado1 = new Empleado("Juan", 'M', true);
        
        //funcionPolimorfismo(persona1);
        funcionPolimorfismo(empleado1);
        
    }
    
    public static void funcionPolimorfismo(Persona args){
        //System.out.println(args.saludar());
        
        if(args instanceof Empleado){
            System.out.println("es empleado");
        }
        
        else if(args instanceof Persona){
            System.out.println("es persona");
            
        }
        
        else if(args instanceof Object){
            System.out.println("es objeto");
        }
    }
}
