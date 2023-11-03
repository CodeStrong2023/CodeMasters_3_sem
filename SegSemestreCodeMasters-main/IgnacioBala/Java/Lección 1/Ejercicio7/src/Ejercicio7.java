
import java.util.Scanner;


public class Ejercicio7 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
               final double SALARIO_BASE = 1000.0; // Salario base constante de $1000
        
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Ingrese el número de carros vendidos: ");
        int carrosVendidos = scanner.nextInt();
        
        System.out.print("Ingrese el valor de venta por carro: $");
        double valorVentaPorCarro = scanner.nextDouble();
        
        double comisionCarrosVendidos = carrosVendidos * 150.0; // Comisión por carros vendidos
        
        double comisionValorVenta = carrosVendidos * valorVentaPorCarro * 0.05; // Comisión por valor de venta
        
        double salarioMensual = SALARIO_BASE + comisionCarrosVendidos + comisionValorVenta;
        
        System.out.println("El salario mensual del vendedor es: $" + salarioMensual);

    }
    
}
