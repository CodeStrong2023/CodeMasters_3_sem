/*
Proyecto caja: 
Ejercicio 1: Crear un proyecto segun especificaciones 
mostradas a continuacion.
La fotma es: Volumen = anchi * alto * profundidad 
 */
package Caja;

public class Caja {
    //Atributos
    int ancho;
    int alto;
    int profundo;
    //constructores(acciones)
    public Caja(){ //constructor1 
    }
    public Caja(int ancho, int alto, int profundo){//constructor2
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
        
    }
    
    public int calcularVolumen(){
        return ancho * alto * profundo;//metodo para calcular
        
    }
}
