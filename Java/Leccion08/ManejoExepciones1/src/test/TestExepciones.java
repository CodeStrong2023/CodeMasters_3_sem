/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package test;

/**
 *
 * @author Virginia
 */
public class TestExepciones {
    public static void main(String[] args) {
        int resultado = 0;
        try {
            resultado = 10/0;
        } catch (Exception e) {
            System.out.println("ocurrió un error");
            e.printStackTrace(System.out); //se conoce como pilas de exepciones
        }
        System.out.println("la variable de resultado tiene como valor: "+resultado);
    }
}
