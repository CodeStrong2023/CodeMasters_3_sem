
package test;

public class TestAutoboxingUnboxing {
    public static void main(String[] args) {
        // Clases envolventes o Wapper 
        
        /*
            Clases envolc=ventes de tipo primitivos
            int = la clase envolvente es integer
            long = la clase envolvente es Long
            float = la clase envolvente es Float
            double = la clase envolvente es Double
            boolean = la clase envolvente es Bolean
            byte = la clase envolvente es Byte
            chat = la clase envolvente es Char
            short = la clase envolvente es short
        */
        
        int enteroPrim = 10; //Tipo primitivo
        System.out.println("enteroPrim = " + enteroPrim);
        Integer entero =  10; // Tipo Objet con la clase integer
        System.out.println("entero = " + entero.byteValue()); //Autoboxing
        
        int entero2 = entero; //Unboxing
        System.out.println("entero2 = " + entero2);
    }
}
