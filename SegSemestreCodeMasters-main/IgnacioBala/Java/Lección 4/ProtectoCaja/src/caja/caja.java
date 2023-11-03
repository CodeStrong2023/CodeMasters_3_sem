
 
package caja;


public class caja {
    int ancho;
    int alto;
    int profundo;
    
    //Métodos y constructores
    public caja(){
        
    }
    //Constructor co parámetros
    public caja(int ancho , int alto, int profundo) {
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }
     public int CalcularVolumen(){
         return ancho * alto * profundo;
     }
}
