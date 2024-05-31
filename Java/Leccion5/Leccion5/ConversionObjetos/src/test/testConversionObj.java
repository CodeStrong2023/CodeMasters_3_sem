
package test;

import domain.*;

/**
 *
 * @author virginia
 */
public class testConversionObj {
    public static void main(String[] args) {
        Empleado empleado1;
        
        empleado1 = new Escritor("Juan", 'H', true, Tipo_Escritura.CLASICO);
        
        //System.out.println(empleado1.obtenerDetaller());
        //System.out.println("empleado1 = " + empleado1);
        
        System.out.println(((Escritor)empleado1).getTipoEscritura());
    }
    
}
