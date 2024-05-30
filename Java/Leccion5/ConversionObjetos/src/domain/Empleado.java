
package domain;

/**
 *
 * @author virginia
 */
public class Empleado extends Persona {
    private int idEmpleado;
    private static int contadorEmpleado;
    
    static{
        ++Empleado.contadorEmpleado;
    }
    
        
    public Empleado(String nombre, char genero, boolean status){
        super(nombre, genero, status);
        this.idEmpleado = Empleado.contadorEmpleado;
    }
    
    public String obtenerDetaller(){
        return "Empleado{" + "idEmpleado=" + idEmpleado + ", " + super.toString() + '}';
    }
    
    @Override
    public String saludar(){
        return ("Hola desde la clase hija");
    }

    @Override
    public String toString() {
        return "Empleado{" + "idEmpleado=" + idEmpleado + ", " + super.toString() + '}';
    }
    
    
    
    
}
