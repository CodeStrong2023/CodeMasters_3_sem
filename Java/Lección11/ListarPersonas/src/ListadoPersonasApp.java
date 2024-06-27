import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class ListadoPersonasApp {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //Definimos lista fuera de ciclo while
        List<Persona> personas = new ArrayList<>();
        //Menú
        var salir = false;
        while(!salir){
            mostrarMenu();
            try{
                salir = ejecutarOperacion(entrada, personas);
            } catch (Exception e){
                System.out.println("Ocurrió un problema: "+ e.getMessage());
            }
            System.out.println();
        }//FIn ciclo while
    }//Fin método main

    private static void mostrarMenu(){
        //Mostramos las opciones
        System.out.print("""
                ******* Listado de Personas *******
                1.Agregar
                2.Listar
                3.Salir
                """);
        System.out.print("Ingrese una de las opciones: ");
    }//Fin método mostarMenú

    private static boolean ejecutarOperacion(Scanner entrada, List<Persona> personas){
        var opcion = Integer.parseInt(entrada.nextLine());
        var salir = false;
        switch (opcion){
            case 1 -> { //Agregar a una persona
                System.out.println("Ingrese el nombre: ");
                var nombre = entrada.nextLine();
                System.out.println("Ingrese el número telefónico: ");
                var tel = entrada.nextLine();
                System.out.println("Ingrese el email: ");
                var email = entrada.nextLine();
                var persona = new Persona(nombre, tel, email);
                personas.add(persona);
                System.out.println("La lista tiene: "+personas.size()+" elementos.");
            } //Fin caso 1
            case 2 -> { //Listar a las personas
                System.out.println("Listado de personas: ");
                //Mejoras con lambda y método de referencia
                //personas.forEach((persona) -> System.out.println(persona));
                personas.forEach(System.out::println);
            } //Fin caso 2
            case 3 -> { //Salir del ciclo
                System.out.println("Hasta pronto!");
                salir =true;
            } //Fin caso 3
            default -> System.out.println("Opción incorrecta: "+opcion);
        } //Fin del switch
        return salir;
    }//Fin de método ejecutarOperacion
}//Fin clase ListadoPersonasApp
