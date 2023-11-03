package CicloWhile;

public class Ejercicio1 {
    public static void main(String[] args) {
        var conteo = 0;
        while (conteo < 3) {
            System.out.println("Conteo = "+conteo);
            conteo++;
        }
        
        var contador = 0;
        do{
            System.out.println("Contador = "+contador);
            contador++;
        }while(contador <= 7);
        
        for(var contando = 0; contando < 7; contando++){
            if(contando % 2 == 0){
                System.out.println("Contando = "+contando);
                break;
            }
        }
        inicio:
         for(var contando = 0; contando < 7; contando++){
            if(contando % 2 != 0){
                continue inicio;
            }
                System.out.println("Contando = "+contando);
         }
    }
    
}
