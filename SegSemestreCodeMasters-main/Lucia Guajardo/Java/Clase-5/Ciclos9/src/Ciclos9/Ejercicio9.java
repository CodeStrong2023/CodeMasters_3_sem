/*Pedir el día, mes y año de una fecha e indicar
si la fecha es correcta,Suponiendo que todos los meses 
son de 30 días.
 */
package Ciclos9;

import java.util.Scanner;

public class Ejercicio9 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese el día: ");
        int dia = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese el número de mes: ");
        int mes = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese el año: ");
        int anio = Integer.parseInt(entrada.nextLine());
        if((dia != 0)&&(dia <= 30)) {
            if((mes != 0)&&(mes <= 12)) {
                if ((anio != 0)&&(anio <= 2022)) {
                    System.out.println("La fecha ingresada es: "+dia+"/"+mes+"/"+anio);
                }
                else {
                    System.out.println("Año incorrecto.");
                }
            }
            else {
                System.out.println("Mes incorrecto.");
            }
        }
        else {
            System.out.println("Fecha incorrecta.");
        }
    }
    
}
