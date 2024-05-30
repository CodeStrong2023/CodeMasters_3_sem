package domain;

public class Persona {
    private String nombre;
    private char genero;
    private boolean status;
    
    public Persona(String nombre, char genero, boolean status){
        this.nombre = nombre;
        this.genero = genero;
        this.status = status;
    }

    public boolean isStatus() {
        return status;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public char getGenero() {
        return genero;
    }

    public void setGenero(char genero) {
        this.genero = genero;
    }
    
    
    public String saludar(){
        return ("Hola desde la clase padre");
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Persona{");
        sb.append("nombre=").append(nombre);
        sb.append(", genero=").append(genero);
        sb.append(", status=").append(status);
        sb.append('}');
        return sb.toString();
    }
    
    
    
    
}
