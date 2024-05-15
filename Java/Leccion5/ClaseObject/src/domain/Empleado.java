/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
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
    
    {
        this.idEmpleado = Empleado.contadorEmpleado;
    
    }
        
    public Empleado(String nombre, char genero, boolean status){
        super(nombre, genero, status);
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
