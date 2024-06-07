
package test;

import domain.Persona;

/**
 *
 * @author Virginia
 */
public class TestJavaBerans {
    public static void main(String[] args){
        Persona persona= new Persona();
        persona.setNombre("Juan");
        persona.serApellido("Perez");
        System.out.println("persona =" + persona);
        
        System.out.println("persona nombre: " +persona.getNombre);
        System.out.println("persona apellido: " +persona.getApellido);
    }
}
