
package test;

import Enumeraciones.Continentes;
import Enumeraciones.Dias;

public class TestEnumeracion {
    public static void main(String[]args){
        //System.out.println("Dia 1: "+Dias.LUNES);
        //indicarDia(Dias.DOMINGO);  // Las enumeraciones se tratan como si fueran cadenas
        System.out.println("Continente N1: "+Continentes.AFRICA);
        System.out.println("Numero de paises del continente: "
                +Continentes.AFRICA.getPaises());
        System.out.println("Numero de habitantes continente: "
                +Continentes.AFRICA.getHabitantes());
        System.out.println("  ");
        
        System.out.println("Continente N2: "+Continentes.EUROPA);
        System.out.println("Numero de paises del continente: "
                +Continentes.EUROPA.getPaises());
        System.out.println("Numero de habitantes del continente: "
                +Continentes.EUROPA.getHabitantes());
        System.out.println("  ");
        
        System.out.println("Continente N3: "+Continentes.AMERICA);
        System.out.println("Numero de paises del continente: "
                +Continentes.AMERICA.getPaises());
        System.out.println("Numero de habitantes del continente: "
                +Continentes.AMERICA.getHabitantes());
        System.out.println("  ");
        
        System.out.println("Continente N 4: "+Continentes.ASIA);
        System.out.println("Numero de paises del continente: "
                +Continentes.ASIA.getPaises());
        System.out.println("Numero de habitantes del continente: "
                +Continentes.ASIA.getHabitantes());
        System.out.println("  ");
        
        System.out.println("Continente N 5: "+Continentes.OCEANIA);
        System.out.println("Numero de paises del continente: "
                +Continentes.OCEANIA.getPaises());
        System.out.println("Numero de habitantes del continente: "
                +Continentes.OCEANIA.getHabitantes());
        System.out.println("  ");
    }
    
    private static void indicarDia(Dias dias){
        switch(dias){
            case LUNES:
                System.out.println("Primer dia de la semana ");
                break;
            case MARTES:
                System.out.println("Segundo dia de la semana ");
                break;
            case MIERCOLES:
                System.out.println("Tercer dia de la semana ");
                break;
            case JUEVES:
                System.out.println("Cuarto dia de la semana ");
                break;
            case VIERNES:
                System.out.println("Quinto dia de la semana ");
                break;
            case SABADO:
                System.out.println("Sexto dia de la semana ");
                break;
            case DOMINGO:
                System.out.println("Septimo dia de la semana ");
                break;
            
        }
    }
}
