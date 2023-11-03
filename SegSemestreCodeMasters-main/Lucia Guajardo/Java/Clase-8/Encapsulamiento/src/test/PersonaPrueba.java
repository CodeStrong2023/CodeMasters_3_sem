package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Lucia", 30.000, false);
        System.out.println("persona1 su nombre es: " +persona1.getNombre());
        persona1.setNombre("Antonella");
        
        System.out.println("persona1 con su nombre modificado: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
    }
    
}
