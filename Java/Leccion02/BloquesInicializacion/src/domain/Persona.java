
package domain;

public class Persona {
    private final int idPersona;
    private static int contadorPersonas;
    
    static{ // bloque de inicializacion estatico
        System.out.println("Ejecucion bloque estatico");
        ++Persona.contadorPersonas;
        // idPersona=10; No es un atributo estatico por esto tenemos un error
    }
    
    { //Bloque de inicializacion NO estatico (contexto dinamico)
        System.out.println("Ejecucion del bloque NO estatico");
        this.idPersona = Persona.contadorPersonas++; //incrementamos el atributo
    }
    
    // Los bloques de inicializacion se ejecutan antes del constructor de la clase
    
    public Persona(){
        System.out.println("Ejecucion del constructor");
    }
    
    public int getIdPersona(){
        return this.idPersona;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + '}';
    }
    
}
