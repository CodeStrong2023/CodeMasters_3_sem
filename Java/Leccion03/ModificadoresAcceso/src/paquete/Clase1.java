
package paquete;

public class Clase1 {
    public String atributoPublic = "Valor atributo publico";
    protected String atributoProtected = "Valor atributo protected";
    
    public Clase1(){
        System.out.println("Constructor publico");
    }
    
    protected Clase1(String atributoPublicp){
        System.out.println("Constructor protected");
    }
    
    public void metodoPublico(){
        System.out.println("Metodo Publico");
    }
    
    protected void metodoProtected(){
        System.out.println("Metodo protected");
    }
}
