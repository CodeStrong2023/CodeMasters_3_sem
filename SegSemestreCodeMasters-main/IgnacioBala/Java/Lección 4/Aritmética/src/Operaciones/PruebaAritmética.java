package Operaciones;

public class PruebaAritmética {
    public static void main(String[] args) {
        var a = 10;
        int b = 7;
        miMetodo();
       Aritmetica aritmetica1 = new Aritmetica( );
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();
        // Para almacenar on y atributos es memoria heap
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
       resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumento =" + resultado);
        
        System.out.println("aritmetica1 a: " + aritmetica1.a);
        System.out.println("aritmetica1 b: " + aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5,8);
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);
        
        Persona persona = new Persona("Ignacio","Bala");
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre : "+persona.nombre);
        System.out.println("Persona apellido : "+persona.apellido);
        
    }
    public static void miMetodo(){
        int a = 10;
        System.out.println("Aquí hay otro método");
        
    }
   
}
 