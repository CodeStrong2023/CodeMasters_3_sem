
import java.util.Scanner;


public class Ejercicio5 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
         Scanner scanner = new Scanner(System.in);
        
        System.out.print("Ingresa la primera calificación: ");
        double calificacion1 = scanner.nextDouble();
        
        System.out.print("Ingresa la segunda calificación: ");
        double calificacion2 = scanner.nextDouble();
        
        System.out.print("Ingresa la tercera calificación: ");
        double calificacion3 = scanner.nextDouble();
        
        double sumaCalificaciones = calificacion1 + calificacion2 + calificacion3;
        
        System.out.println("La suma total de las calificaciones es: " + sumaCalificaciones);
    }
    
}
