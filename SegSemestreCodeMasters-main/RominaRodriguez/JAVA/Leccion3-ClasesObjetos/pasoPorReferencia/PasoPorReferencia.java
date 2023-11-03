//Paso por referencia
package pasoPorReferencia;

import clases.Persona;


public class PasoPorReferencia {
    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.nombre = "Ester";
        System.out.println("persona1 nombre = " + persona1.nombre);
        cambiarValor(persona1);
        System.out.println("El cambio que hicemos en el nombre es: "+persona1.nombre);
    }
    
    public static void cambiarValor(Persona persona){//paso por referencia
        persona.nombre = "Maria";
        
    }
}
