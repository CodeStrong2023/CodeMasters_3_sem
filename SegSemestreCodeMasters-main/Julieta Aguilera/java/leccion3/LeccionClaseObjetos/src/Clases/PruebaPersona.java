
package Clases;


public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1;
        persona1 = new Persona(); //Llamamos al constructor
        persona1.nombre = "Julieta"; //El valor hexagesimal normalmente comienza con 0x
        persona1.apellido = "Aguilera";
        persona1.obtenerInformacion();
        
        Persona persona2 = new Persona();
        System.out.println("persona2 =" +persona2);
        System.out.println("persona1 =" +persona1);
        persona2.obtenerInformacion();
        persona2.nombre = "Matias";
        persona2.apellido = "Chox";
        persona2.obtenerInformacion();
    }
}
