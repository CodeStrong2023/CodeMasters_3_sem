import java.util.Scanner;

public class Rectangulo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Ingrese la longitud del lado l del rectángulo:");
        double l = sc.nextDouble();

        System.out.println("Ingrese la longitud del lado w del rectángulo:");
        double w = sc.nextDouble();

        double area = l * w;
        double perimetro = 2 * (l + w);

        System.out.println("El área del rectángulo es: " + area);
        System.out.println("El perímetro del rectángulo es: " + perimetro);

        System.out.println("Ingrese el primer número:");
        int num1 = sc.nextInt();

        System.out.println("Ingrese el segundo número:");
        int num2 = sc.nextInt();

        int mayor = (num1 > num2) ? num1 : num2;

        System.out.println("El número mayor es: " + mayor);
        
        
    }
    
}