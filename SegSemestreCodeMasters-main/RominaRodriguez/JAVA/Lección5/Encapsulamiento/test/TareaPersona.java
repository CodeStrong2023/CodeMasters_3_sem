
package test;

import dominio.Persona;

public class TareaPersona {
    public static void main(String[] args) {
        //Creamos el objeto para persona2
        Persona persona2 = new Persona("Romina",25.500, true);
        System.out.println("persona2 su nombre es: "+persona2.getNombre());
        //Modificamos argumentos y vemos en pantalla
        persona2.setNombre("Mariana");
        System.out.println("persona2 con su nombre modificado es: "+persona2.getNombre());
        System.out.println("persona2 el resultado para sueldo es de:$  "+persona2.getSueldo());
        System.out.println("persona2 para obtener booleano: "+persona2.isEliminado());
      
    }
    
}
