/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package test;

import domain.FiguraGeometrica;
import domain.Rectangulo;

/**
 *
 * @author virginia
 */
public class TestClasesAbstractas {

    public static void main(String[] args) {
        FiguraGeometrica fig1 = new Rectangulo("rectangulo");

        fig1.dibujarFigura();

    }
}
