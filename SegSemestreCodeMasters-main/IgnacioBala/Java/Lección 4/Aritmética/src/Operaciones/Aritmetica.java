package Operaciones;

public class Aritmetica {
    // Campos de la clase
    int a;
    int b;

    public Aritmetica(){
        System.out.println("Ejecutando constructor n1");
    }
    // Constructor que recibe dos argumentos para inicializar 'a' y 'b'
    public Aritmetica(int a, int b) {
        this.a = a;
        this.b = b;
        System.out.println("Se ejecuta constructor n2");
    }
        

    // Método para sumar 'a' y 'b' y mostrar el resultado
    public void sumarNumeros() {
        System.out.println("Suma: " + (a + b));
    }

    // Método para sumar 'a' y 'b' y retornar el resultado
    public int sumarConRetorno() {
        return a + b;
    }

    // Método que recibe dos argumentos, los suma y retorna el resultado
   public int sumarConArgumentos(int a, int b) {
    return a + b;
}
    }

class Persona {
    String nombre;
    String apellido;
    
    
    
    Persona(String nombre , String apelido){
        super(); // Llamada al constructor de la clase padre object
        this.nombre = nombre;
        //Imprimir imprimir = new Imprimir();
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: "+this);
    }
}

class Imprimir{
    public Imprimir(){
            super(); 
    }
    public void imprimir(Persona persona){
        System.out.println("Impresion del objeto actual (this):"+this); 
    }
}