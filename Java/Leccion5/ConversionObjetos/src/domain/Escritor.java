
package domain;

/**
 *
 * @author virginia
 */
public class Escritor extends Empleado {
    
    final Tipo_Escritura tipoEscritura;
    
    public Escritor(String nombre, char genero, boolean status, Tipo_Escritura tipoEscritura){
        super(nombre, genero, status);
        this.tipoEscritura = tipoEscritura;
        
    }

    public Tipo_Escritura getTipoEscritura() {
        return tipoEscritura;
    }

        @Override
    public String obtenerDetaller(){
        return super.obtenerDetaller()+ "Tipo Escritura: "+ this.tipoEscritura.getDescripcion();
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Escritor{");
        sb.append("tipoEscritura=").append(tipoEscritura);
        sb.append("DatosEmpleado=").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
    
    
    
}
