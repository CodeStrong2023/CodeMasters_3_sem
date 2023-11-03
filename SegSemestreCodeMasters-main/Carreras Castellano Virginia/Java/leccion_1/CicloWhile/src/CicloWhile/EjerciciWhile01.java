package CicloWhile;

public class EjerciciWhile01 {

    public static void main(String[] args) {
        var conteo = 0; //inferencias de tipos
        while (conteo <= 7) {
            System.out.println("conteo = " + conteo);
            conteo++; //vamos incremetando la variaable    
        }
        var contador = 0;
        do {
            System.out.println("contador = " + contador);
            contador++;
        } while (contador < 7);
        //uso de las palabras break y continue junto a las estiquetas(labels)
        //inicio:
        for (var contando = 0; contando < 7; contando++) {// (aca se declara la variable, aca la condicion,incremento o decremento ,iterador)
            if (contando % 2 == 0) {
                System.out.println("contando = " + contando);
                break /*inicio*/ ; 
            }
        }

        inicio:
        for (var contando = 0; contando < 7; contando++) {// (aca se declara la variable, aca la condicion,incremento o decremento ,iterador)
            if (contando % 2 != 0) {
                continue inicio; //vamos a la siguiente iteración
            }
            System.out.println("contando = " + contando);
        }
    }
}
