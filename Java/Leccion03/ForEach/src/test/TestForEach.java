
package test;

import domain.Persona;

public class TestForEach {
    public static void main(String[] args) {
        int edades[] = {5, 6, 7, 8, 9}; //Sintaxis resumida
        for (int edad: edades) { //Sintaxis ForEach
            System.out.println("edad = " + edad);
        }
        
        Persona personas[] = {new Persona("Juan"), new Persona("Julieta"), new Persona("Matias")};
        
        //ForEach
        for(Persona persona: personas){
            System.out.println("persona = " + persona);
        }
        
        
    }
    
}
