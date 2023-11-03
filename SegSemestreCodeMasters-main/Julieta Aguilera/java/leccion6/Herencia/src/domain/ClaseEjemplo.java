
package domain;

public class ClaseEjemplo {
    public ClaseEjemplo(){
    }
    
    public String getNameAndLastName(){ 
        Persona persona = new Persona();
        String nombreapellido = persona.getNombre() +" "+persona.getApellido();
        return nombreapellido;
        
    }
}
