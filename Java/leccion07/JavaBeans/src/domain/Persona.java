
package domain;

/**
 * @author Virginia
 */
public class Persona {
    private String nombre;    
    private String apellido;
    public String getNombre;
    public String getApellido;
    
    //constructor vacio: esto es ibligatorio
    public  Persona(){
    
    }
    public  Persona(String nombre, String apellido){
        this.nombre= nombre;
        this.apellido= apellido;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    @Override
    public String toString() {
        return "persona{" + "nombre=" + nombre + ", apellido=" + apellido + '}';
    }

    public void serApellido(String perez) {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }
    
}
