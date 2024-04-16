
package Test;

public class TestArgumentosVariables {
    public static void main(String[] args){
        imprimirNumeros(3, 4,5,6);
        imprimirNumeros(1,2,7);
        variosParametros("Luciana "," Castro ", 7,8,9);
    }
    private static void variosParametros(String nombre,String Apellido, int ...numeros){  // El argumento variable va siempre al final
        System.out.print("Nombre: "+nombre);
        System.out.print("Apellido: "+Apellido);
        imprimirNumeros(numeros);
    }
    private static void imprimirNumeros(int ...numeros){
        for(int i = 0; i < numeros.length; i++){
            System.out.println("Elementos: "+numeros[i]);
        }  
    }
}
