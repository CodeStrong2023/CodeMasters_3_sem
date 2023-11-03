
package Operaciones;

public class Aritmetica {
    //Atributos de la clase
    int a;
    int b;

    //El constructor es un metodo especial
    public Aritmetica(){ //Constructor 1
        System.out.println("Se esta ejecutando este contructor numero uno");
    }

    public Aritmetica(int a, int b){
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando este constructor numero dos");
    }
    //Metodo
    public void sumarNumeros() {
        int resultado = a + b;
        System.out.println("resultado = "+ resultado);
    }

    public int sumaConRetorno(){
        // int resultado = a + b;
        return a + b;
    }

    public int sumarConArgumentos(int a, int b){
        this.a = a; //El argumento a se asigna al atributo this.a
        this.b = b;
        // return a + b;
        return this.sumaConRetorno();
    }
}
