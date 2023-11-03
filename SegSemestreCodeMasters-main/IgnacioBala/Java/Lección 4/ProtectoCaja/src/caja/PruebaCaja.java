    
package caja;


public class PruebaCaja {
    public static void main(String[] args) { //Método main
            // Crear objetos de caja utilizando diferentes constructores
        caja caja1 = new caja(); // Utiliza el constructor sin parámetros
        caja caja2 = new caja(10, 5, 3); // Utiliza el constructor con parámetros

        // Configurar dimensiones para el primer objeto
        caja1.ancho = 7;
        caja1.alto = 4;
        caja1.profundo = 2;

        // Calcular el volumen de ambas cajas
        int volumenCaja1 = caja1.CalcularVolumen();
        int volumenCaja2 = caja2.CalcularVolumen();

        // Mostrar el volumen de cada caja
        System.out.println("Volumen de la primera caja: " + volumenCaja1);
        System.out.println("Volumen de la segunda caja: " + volumenCaja2);
    }

        
    }
