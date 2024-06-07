/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package domain;

/**
 *
 * @author virginia
 */
public class Rectangulo extends FiguraGeometrica {

    public Rectangulo(String tipoFigura) {
        super(tipoFigura);
    }

    @Override
    public void dibujarFigura() {
        System.out.println("dibuja un rectangulo: " + this.getClass().getSimpleName());
    }
}
