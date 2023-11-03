/*
Ejercicio 9: Pedir el dia, mes y año de una fecha 
e indicar si la fecha es corecta. Suponiendo que 
todos los meses son de 30 días
*/
package Ciclo09;

import java.util.Scanner;


public class Ciclo09 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el día: ");
        int dia = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el mes: ");
        int mes = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el año: ");
        int año= Integer.parseInt(entrada.nextLine());
        if((dia != 0)&&(dia <= 30)){
            if((mes != 0)&&(mes <= 12)){
                if((año != 0)&&(año <= 2022)){
                    System.out.println("La fecha ingresada es: "+dia+"/"+mes+"/"+año);
                }
                else{
                    System.out.println("Fecha incorrecta, año incorrectos");
                }
            }    
            else{
                  System.out.println("Fecha incorrecta, mes incorrecto");
                }
        }    
        else{
            System.out.println("Fecha incorecta, dia incorrecto");
        }
        
    }
}
