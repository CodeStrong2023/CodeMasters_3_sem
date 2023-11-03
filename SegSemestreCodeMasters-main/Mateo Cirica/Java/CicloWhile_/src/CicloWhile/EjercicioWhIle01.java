package CicloWhile;


public class EjercicioWhIle01 {
    public static void main(String[] args) {
        var conteo = 0; //Inferencia de tipos
        while(conteo < 7){
            System.out.println("conteo = " + conteo);
            conteo++; 
        }
        System.out.println("");
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador < 7);

        System.out.println("");

        for(var c = 0; c < 7; c++){
            if(c % 2 == 0){
                 System.out.println("contando = " + c);
                 break;
            }
        }

        for(var c = 0; c < 7; c++){
            if(c % 2 != 0){
                continue;
            }
         System.out.println("contando = " + c);
        }

    }
}