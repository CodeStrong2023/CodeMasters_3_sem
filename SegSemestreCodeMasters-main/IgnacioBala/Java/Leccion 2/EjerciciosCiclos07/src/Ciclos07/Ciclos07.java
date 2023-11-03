/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ciclos07;

import java.util.Scanner;

/**
 *
 * @author Usuario
 */
public class Ciclos07 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero,conteo = 0, suma = 0 ;
        float promedio = 0;
        System.out.println("Digite un número");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero>=0){ //Mientras el número no sea negativo
            suma+= numero;
            conteo++;
            numero = Integer.parseInt(entrada.nextLine());
        }
                
            if(conteo== 0){
                System.out.println("\nError, la división entre 0 no existe ");
            }
            else{
                promedio = (float)suma/conteo;
                        System.out.println("promedio = " + promedio);
            }
    }
}
