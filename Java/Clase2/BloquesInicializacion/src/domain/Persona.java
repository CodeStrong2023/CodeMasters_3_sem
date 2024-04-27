package domain;

public class Persona {
    private final int idPersona;
    private static int contadorPersonas;
    
    static {
        System.out.println("Ejecución del bloque estático");
        ++Persona.contadorPersonas;
        //idPersona=10; no es estático un atributo, por eso tenemos un error
    }
    
    {//Bloque de inicialización no estático (contexto dinámico
        System.out.println("Ejecución del bloque no estático");
        this.idPersona = Persona.contadorPersonas++;
    }
    
    public Persona(){
        System.out.println("Ejecución del constructor");
    }
    public int getIdPersona(){
        return this.idPersona;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + '}';
    }
    
    
}
