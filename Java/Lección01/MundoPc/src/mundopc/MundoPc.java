
package mundopc;

import ar.com.system2023.mundopc.*;

public class MundoPc {
    public static void main(String[] args) {
        Monitor monitorHP = new Monitor("HP", 13);//Importar la clase
        Teclado tecladoHP = new Teclado("Bluetooth", "HP");
        Raton ratonHP = new Raton("Bluetooth", "HP");
        Computadora computadoraHP = new Computadora("computadora HP", monitorHP, tecladoHP, ratonHP);
        
        
        Monitor monitorGamer = new Monitor("Gamer", 32);//Importar la clase
        Teclado tecladoGamer = new Teclado("Bluetooth", "Gamer");
        Raton ratonGamer = new Raton("Bluetooth", "Gamer");
        Computadora computadoraGamer = new Computadora("computadora Gamer", monitorGamer, tecladoGamer, ratonGamer);
        
            
        //Crear más objetos de tipo computadora con todos los elementos

        Monitor monitorApple = new Monitor("Apple", 17);//Importar la clase
        Teclado tecladoApple = new Teclado("Bluetooth", "Apple");
        Raton ratonApple = new Raton("Bluetooth", "Gamer");
        
        Monitor monitorLenovo = new Monitor("Lenovo", 20);//Importar la clase
        Teclado tecladoLenovo = new Teclado("Bluetooth", "Lenovo");
        Raton ratonLenovo = new Raton("Bluetooth", "Lenovo");
        
        Monitor monitorAsus = new Monitor("Asus", 20);//Importar la clase
        Teclado tecladoAsus = new Teclado("Bluetooth", "Asus");
        Raton ratonAsus = new Raton("Bluetooth", "Asus");
        
        Monitor monitorDell = new Monitor("Dell", 27);//Importar la clase
        Teclado tecladoDell = new Teclado("Bluetooth", "Dell");
        Raton ratonDell = new Raton("Bluetooth", "Dell");
    

        
        //Agregamos más elementos a la lista orden1
        
        Computadora computadoraApple = new Computadora("Computadora Apple", monitorApple, tecladoApple, ratonApple);
        Computadora computadoraLenovo = new Computadora("Computadora Lenovo", monitorLenovo, tecladoLenovo, ratonLenovo);
        Computadora computadoraAsus = new Computadora("Computadora Asus", monitorAsus, tecladoAsus, ratonAsus);
        Computadora computadoraDell = new Computadora("Computadora Dell", monitorDell, tecladoDell, ratonDell);
        Computadora computadorasVarias1= new Computadora("Computadora de diferente marcas", monitorApple, tecladoGamer, ratonHP);
        Computadora computadorasVarias2 = new Computadora("Computadora de diferente marcas", monitorDell, tecladoApple, ratonLenovo);
        Computadora computadorasVarias3 = new Computadora("Computadora de diferente marcas", monitorAsus, tecladoGamer, ratonDell);
        Computadora computadorasVarias4 = new Computadora("Computadora de diferente marcas", monitorApple, tecladoAsus, ratonHP);
        
        //completar una lista en el objeto orden1 que llegue a los 10 elementos
        //Creo una lista de computadoras para agregar a al orden
        Computadora[] computadoras = {
            computadoraHP,
            computadoraGamer,
            computadoraApple,
            computadoraLenovo,
            computadoraAsus,
            computadoraDell,
            computadorasVarias1,
            computadorasVarias2,
            computadorasVarias3,
            computadorasVarias4,
        };
      
        Orden orden1 = new Orden();//inicializamos el arreglo vacio
        Orden orden2 = new Orden();//Una nueva lista con objeto orden2
        
        //con un ciclo for agrego la lista de las computadoras a la orden1, para optimizar el código
        for (Computadora computadora : computadoras) {
            orden1.agregarComputadora(computadora);
        }
        
        Computadora computadorasVarias = new Computadora("Computadora de diferente marcas", monitorHP, tecladoGamer, ratonHP);
        orden2.agregarComputadora(computadorasVarias);
        
        orden1.mostrarOrden();
        orden2.mostrarOrden();
        
        //Crear más objetos de tipo computadora con todos los elementos
        //completar una lista en el objeto orden1 que llegue a los 10 elementos
        //probar de esta manera los objetos al máximo rendimiento
    }
}
