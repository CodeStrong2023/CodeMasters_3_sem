
import java.util.Scanner;



/**
 *
 * @author Usuario
 */
public class Ejercicio6 {
    
    public static void main(String[] args) {
          Scanner scanner = new Scanner(System.in);
        
        System.out.print("Ingrese la cantidad de dinero que tiene Guillermo: $");
        double guillermo = scanner.nextDouble();
        
        double luis = guillermo / 2;
        double juan = (guillermo + luis) / 2;
        
        double totalDinero = guillermo + luis + juan;
        
        System.out.println("La cantidad de dinero total entre los tres es: $" + totalDinero);
        // TODO code application logic here
    }
    
}
