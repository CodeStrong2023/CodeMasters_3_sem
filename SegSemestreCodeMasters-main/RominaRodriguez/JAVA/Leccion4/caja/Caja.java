
package caja;//Package


public class Caja {//Clase publica caja
    //Atributos(características)
    int ancho;
    int alto;
    int profundo;
    //Método constructor(acciones)
    public Caja(){//Contructor 1 = vacio
    }
    //Constructor con parámetros
    public Caja(int ancho, int alto, int profundo){//Constructor 2
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }
    public int calcularVolumen(){//Método para calcular
        return ancho * alto * profundo;
    }
    
}
