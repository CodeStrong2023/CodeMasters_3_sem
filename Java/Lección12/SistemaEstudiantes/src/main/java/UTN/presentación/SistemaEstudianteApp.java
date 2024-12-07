package UTN.presentación;
import UTN.datos.EstudianteDAO;
 import UTN.dominio.Estudiante;
import UTN.conexion.Conexion;

import java.sql.SQLOutput;
import java.util.Scanner;

public class SistemaEstudianteApp {
    public static void main(String[] args) {
        var salir = false;
        var  consola = new Scanner(System.in);
        var estudianteDao = new EstudianteDAO();
        while (!salir){
            try {
                mostrarMenu();
                salir = ejecutarOpciones(consola,estudianteDao);

            }catch (Exception e){
                System.out.println("Ocurrió un error al ejecutar operacion: "+e.getMessage());
            }
        }

    }
} // Fin Main

private static void mostrarMenu(){
    System.out.println("""
            
    *** Sistemas de estudiantes***
    1.Listar estudiantes
    2.Buscar estudiantes
    3.Agregar estudiante
    4.Modificar estudiante
    5.Eliminar estudiante
    6.Salir

    Elige una opción:
     """);
}