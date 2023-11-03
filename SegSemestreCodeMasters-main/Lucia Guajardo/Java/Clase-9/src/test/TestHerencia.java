package test;

import domain.ClaseEjemplo;
import domain.Cliente;
import domain.Empleado;
import java.util.Date;

public class TestHerencia {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Lucia", 57000.00);
        System.out.println("empleado1 = " + empleado1);
        ClaseEjemplo claseEjemplo = new ClaseEjemplo();
        System.out.println("Nombre y Apellido: " + claseEjemplo.getNameAndLastName());
        
        Cliente cliente = new Cliente(new Date(), true, "Rosi", 'F', 22, "San Rafael");
        System.out.println("cliente = " + cliente);
    }
    
}