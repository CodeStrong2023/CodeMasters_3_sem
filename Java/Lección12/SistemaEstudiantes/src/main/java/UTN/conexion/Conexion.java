package UTN.conexion;


import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Conexion {
    public static Connection getConnection() {
        Connection conexion = null;
        // Vartiables para conectarnois a bsd
        var baseDatos = "estudiantes";
        var url = "jdbc:mysql://localhost:3306/" + baseDatos;
        var usuario = "root";
        var password = "Monito1234@";
        // Cargamos la clase del driver de mysql
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            conexion = DriverManager.getConnection(url, usuario, password);
            } catch (ClassNotFoundException | SQLException e){
            System.out.println("Ocurrió un eror en la conexion"+ e.getMessage());
              }//Fin catch
        return conexion;

        } //Fin método  connexion
    }