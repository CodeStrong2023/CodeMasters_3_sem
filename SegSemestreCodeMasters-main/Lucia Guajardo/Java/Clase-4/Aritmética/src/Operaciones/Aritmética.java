
package Operaciones;


public class Aritmética {
    int a;
    int b; 
    
    public Aritmética() {
        System.out.println("Se está ejecutando este constructor número uno");
    }
    
    public Aritmética(int a, int b) {
        this.a = a;
        this.b = b;
        System.out.println("Se está ejecutando este constructor número dos");
    }
    
    public void sumarNumeros() {
        int resultado =a + b;
        System.out.println("Resultado = "+resultado);
    }
    
    public int sumarConRetorno() {
        return a + b;
    }
    
    public int sumarConArgumentos(int arg1, int arg2){
        this.a = arg1;
        this.b = arg2;
        //return a + b;
        return this.sumarConRetorno();
    }
}
