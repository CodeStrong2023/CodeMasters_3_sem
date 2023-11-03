
package Operaciones;


public class pruebaAritmetica {
    public static void main(String[] args) {
        Aritmética aritmetica1 = new Aritmética();
        aritmetica1.a =3;
        aritmetica1.b=7;
        aritmetica1.sumarNumeros();
        
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("Resultado = "+resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = "+resultado);
        
        System.out.println("aritmetica1 a: "+aritmetica1.a);
        System.out.println("aritmetica1 b: "+aritmetica1.b);
        
        Aritmética aritmetica2 = new Aritmética(5, 8);
        System.out.println("aritmetica2  a: "+aritmetica2.a);
        System.out.println("aritmetica2  b: "+aritmetica2.b);
    }
}
