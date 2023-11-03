
public class HolaMundo {

    public static void main(String[] args) {
    /*    System.out.println("Hola mundo desde java");
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        //Tipo string
        String miVariableCadena =  "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programación";
        System.out.println(miVariableCadena);
 
     var miVaribaleEntera2= 10;
     var miVaribaleCadena2 = "Seguimos estudiando" ;
        System.out.println("miVaribaleEntera2 = " + miVaribaleEntera2);
        System.out.println("miVaribaleCadena2 = " + miVaribaleCadena2);*/

  /*var usuario = "Osvaldo";
  var titulo = "Ingeniero";
  var union = titulo + usuario;
  int personaId = 1 ;
        int num1 = 5, num2 = 4;
        var solucion = num1 + num2;
        System.out.println("solucion suma = " + solucion);
        solucion = num1 - num2;
        System.out.println("solucion resta = " + solucion);
        solucion = num1 * num2;
        System.out.println("solucion multiplicación = " + solucion);
        solucion = num1 / num2;
        System.out.println("solucion division = " + solucion );
        var solucion2 = 3.4/ num2;
        System.out.println("solucion2 = " + solucion2);
        solucion = num1 %  num2;
        System.out.println("solucion residuo = " + solucion);
        if (num1%2==0)
            System.out.println("Es un número par");
        else 
            System.out.println("Es un número impar");
         byte numEnteroByte = 127;
//        System.out.println("numEnteroByte = " + numEnteroByte);
//        System.out.println("Valor minimo del Byte:"+ Byte.MIN_VALUE);
//        System.out.println("Valor maximo del Byte:"+ Byte.MAX_VALUE);
//        
//        short numEnteroShort = 32767;
//        System.out.println("numEnteroShort = " + numEnteroShort);
//        System.out.println("Valor minimo del Short:"+ Short.MIN_VALUE);
//        System.out.println("Valor maximo del Short:"+ Short.MAX_VALUE);
//        
//        int numEnteroInt = 2147483647;
//        System.out.println("numEnteroInt = " + numEnteroInt);
//        System.out.println("Valor minimo del int:"+ Integer.MIN_VALUE);
//        System.out.println("Valor maximo del int:"+ Integer.MAX_VALUE);
//        
//        long numEnteroLong = 9223372036854775807L;
//        System.out.println("numEnteroLong = " + numEnteroLong);
//        System.out.println("Valor minimo del long:"+ Long.MIN_VALUE);
//        System.out.println("Valor maximo del long:"+ Long.MAX_VALUE);
//        
//       float numFloat = 3.4028235E38F;
//        System.out.println("numFloat = " + numFloat);
//        System.out.println("El valor minimo de float:"+ Float.MIN_VALUE);
//        System.out.println("El valor maximo de float:"+ Float.MAX_VALUE);
//        
//        double numDouble = 1.7976931348623157E308D;
//        System.out.println("numDouble = " + numDouble);
//        System.out.println("El valor minimo de double:"+ Double.MIN_VALUE);
//        System.out.println("El valor maximo de double:"+ Double.MAX_VALUE);
//        
//     
//        
//       var numEntero = 20;
//       System.out.println("numEntero - " + numEntero );
//       var numFloat - 10.0;
//        System.out.println("numFloat - " + numFloat);
//       
//      char miVariableChar = 'a';
//        System.out.println("miVariableChar = " + miVariableChar);
//        
//        char varCaracter = '\u0024';
//        System.out.println("varCaracter = " + varCaracter);
//        char varCaracterDecimal = 36;
//        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
//        char varCaracterSimbolo = '$';
//        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
//        
//        int varEnteroChar = '$';
//        System.out.println("varEnteroChar = " + varEnteroChar);
//        int caracterChar = 'b';
//        System.out.println("caracterChar = " + caracterChar);
//        
//        
//      
//
//        boolean varBool = true;
//        System.out.println("varBool = " + varBool);
//        
//        if(varBool) {
//            System.out.println("La bandera es verde");
//            
//            
//             }
//            
//        else{
//            System.out.println("La bandera es roja"); 
//        }
//        
//        var edad = 30;
//        var adulto = edad >- 18;
//        if (adulto){
//            System.out.println("Eres mayor de edad");
//        }
//        else{
//            System.out.println("Eres menor de edad");
//      
//     
//        }
//      
//      
//         
//        var edad = "20";
//        System.out.println("edad = " + (edad + 1));
//        var valorPT = Double.parseDouble("3.1416");
//        System.out.println("valorPT = " + valorPT);
//        
        var entrada = new Scanner(System.in);
//        System.out.println("Digite su edad:");
//        edad = Integer.parseInt( entrada.nextLine())
//        System.out.println("edad = " + edad);
//        
//        

        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "programadores".charAt(4);
        System.out.println("fraseChar = " + fraseChar);
        
        System.out.println("Digite un caracter: ");
        fraseChar = entrada.nextLine().charAt(0);
        System.out.println("fraseChar = " + fraseChar);
        
        
        
        int num1 = 5, num2 = 4;
        var solucion = num1 + num2;
        System.out.println("solucion de la suma = " + solucion);
        
        solucion = num1  -  num2;
        System.out.println("solucion de la resta = " + solucion);   
        
        solucion = num1 * num2;
        System.out.println("solucion de la multiplicacion = " + solucion);
        
        solucion = num1 / num2;
        System.out.println(" solucion de la divisiion = " +  solucion);
        
        var solucion2 = 3.4 / num2;
        System.out.println("solucion2 resultado de la division = " + solucion2);
        
        solucion = num1 % num2;
        System.out.println("solucion = " + solucion);
        
        if (num1 % 2 == 0)
            System.out.println("es un numero par");
        else
            System.out.println("es un numero impar");
        
         int varNum1 = 1, varNum2 = 4;
        int varNum3 = varNum1 + 6 - varNum2;
        System.out.println("varNum3 = " + varNum3);
        
        varNum1 += 1;
        System.out.println("varNum1 = " + varNum1);
        
        varNum2 -= 2;
        System.out.println("varNum2 = " + varNum2);
        varNum1 *= 5;
        System.out.println("varNum1 = " + varNum1);
        varNum3 /= 4;
        System.out.println("varNum3 = " + varNum3);
        varNum1 %- 6;
        System.out.println("varNum1 = " + varNum1);
        
        
        
        var varA = 7;
        var varB = -varA;
        System.out.println("varA = " + varA);
        System.out.println("varB = " + varB);
        
        var varC = true;
        var varD = !varC;
        System.out.println("varC = " + varC);
        System.out.println("varD = " + varD);
        
        var varE = 9;
        var varF = ++varE;
        System.out.println("varE = " + varE);
        System.out.println("varF = " + varF);
        
        var varG = 3;
        var varH = varG++;
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);
         
        var varK = 8;
        var varL = varK--;
        System.out.println("varK = " + varK);
        System.out.println("varL = " + varL);
*/
  
  
  
  
  
     }
    
}



  
  
