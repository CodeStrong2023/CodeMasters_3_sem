/*Ejercicio 1: Crear un proyecto según las especificaciones
mostradas a continuación.
La formula es: volúmen = ancho * alto * profundidad.
*/
package caja;


public class Caja {
    
    int ancho;
    int alto;
    int profundidad;
    
    public Caja(int ancho, int alto, int profundidad) {
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
    }

    
    public int calcularVolumen() {
        return ancho * alto * profundidad;
    }
}
