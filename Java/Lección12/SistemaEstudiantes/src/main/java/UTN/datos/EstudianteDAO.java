package UTN.datos;

import UTN.dominio.Estudiante;

import static UTN.conexion.Conexion.getConnection;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLOutput;
import java.util.ArrayList;
import java.util.List;

public class EstudianteDAO {
    //Metodo listar
    public List<Estudiante> listarEstudiantes(){
        List<Estudiante> estudiantes = new ArrayList<>();
        //Creamos algunos objetos que son necesarios para comunicranos con la base de datos
        PreparedStatement ps; //Envia sentencis
        ResultSet rs; //Obtenemos resultado
        //Creamos objeto de tipo conexion
        Connection con = getConnection();
        String sql = "SELECT * FROM estudiantes2022 ORDER BY idestudiantes2022";
        try {
            ps = con.prepareStatement(sql);
            rs = ps.executeQuery();
            while ((rs.next())) {
                var estudiante = new Estudiante();
                estudiante.setIdEstudiante(rs.getInt("idestudiantes2022"));
                estudiante.setNombre(rs.getString("nombre"));
                estudiante.setApellido(rs.getString("apellido"));
                estudiante.setTelefono(rs.getString("telefono"));
                estudiante.setEmail(rs.getString("email"));
                //Falata agregarlo a la lista
                estudiantes.add(estudiante);
            }
        } catch (Exception e){
            System.out.println("Ocurrió un error al seleccionar datos: "+e.getMessage());
        }
        finally {
            try {
                con.close();
            } catch (Exception e){
                System.out.println("Ocurriói un error al cerra la conexión: "+e.getMessage());
            }
        }//Fin finally
        return estudiantes;
    }//Fin metodo listar

    //Método por is -> fin bgy id
    public boolean buscarEstudiantesPorId(Estudiante estudiante){
         PreparedStatement ps;
         ResultSet rs;
         Connection con = getConnection();
         String sql = "SELECT * FROM estudiantes2022 WHERE idestudiantes2022=?";
         try {
             ps = con.prepareStatement(sql);
             ps.setInt(1, estudiante.getIdEstudiante());
             rs = ps.executeQuery();
             if(rs.next()){
                 estudiante.setNombre(rs.getString("nombre"));
                 estudiante.setApellido(rs.getString("apellido"));
                 estudiante.setTelefono(rs.getString("Telefono"));
                 estudiante.setEmail(rs.getString("Email"));
                 return true; // Se encuentra registro devuelve verdasdero
             } //Fin If
         } catch (Exception E) {
             System.out.println("Ocurrió un error al buscar estudiante: "+E.getMessage());
         }
         finally {

            try {
                con.close();
            } catch (Exception e){
                System.out.println("Ocurrió un erro al cerra la conexion: "+e.getMessage());
            }//Fin catch
         }//Fin finally
        return false;
    }


    //Método agregar nuevo estudiante
    public boolean agregarEstudiante(Estudiante estudiante){
        PreparedStatement ps;
        Connection con = getConnection();
        String sql = "INSERT INTO estudiantes2022 (nombre, apellido ,telefono, email) VALUES (?,?,?,?)";
        try {
            ps = con.prepareStatement(sql);
            ps.setString(1,estudiante.getNombre());
            ps.setString(2, estudiante.getApellido());
            ps.setString(3, estudiante.getTelefono());
            ps.setString(4 ,estudiante.getEmail());
            ps.execute();
            return true;
        }catch (Exception e){
            System.out.println("Ocurrió un error al agregra estudiante");
        } //FIN CATCH
        finally {
            try {
                con.close();
            }catch (Exception e){
                System.out.println("Erro al cerro conexion: "+e.getMessage());
            } //Fin catch
        } //Fin finally
        return false;
    } // FIN METODO AGREGAR ESTUDIANTE

    //Modificr estudiante
    public boolean modificarEstudiante(Estudiante estudiante){
        PreparedStatement ps;
        Connection con = getConnection();
        String sql = "UPDATE estudiantes2022 SET nombre=?, apellido=?, telefono=?, email=? WHERE idestudiantes2022=?";
        try {
            ps = con.prepareStatement(sql);
            ps.setString(1, estudiante.getNombre());
            ps.setString(2, estudiante.getApellido());
            ps.setString(3, estudiante.getTelefono());
            ps.setString(4, estudiante.getEmail());
            ps.setInt(5,estudiante.getIdEstudiante());
            ps.execute();
            return true;
        }catch (Exception e){
            System.out.println("Erro al modoficar estudante: "+ e.getMessage());
        }// Fin catch
        finally {
            try {
                con.close();
            }catch (Exception e){
                System.out.println("Error al cerrar la conexion"+e.getMessage());
            }//fin catch
        }//fin finally
        return false;
    }//FIN METODO MODIFICAR ESTUDIANTE

    public boolean eliminarEstudiante(Estudiante estudiante){
        PreparedStatement ps;
        Connection con = getConnection();
        String sql = "DELETE FROM estudiantes2022 WHERE idestudiantes2022=?";
        try {
            ps = con.prepareStatement(sql);
            ps.setInt(1,estudiante.getIdEstudiante());
            ps.execute();
            return true;

        }catch (Exception e){
            System.out.println("Error al eliminar esrtudiante: "+e.getMessage());

        }
        finally {
            try {
                con.close();

            }catch (Exception e){
                System.out.println("Error al cerrar la conexiíon: "+e.getMessage());
            }
            return false;
        }
    }



    public static void main(String[] args) {
        var estudianteDao = new EstudianteDAO();
        //MOdificar estudiantes
        var estudiantesModificados = new Estudiante(1,"Carla","Roldan","4343432423523","lonch@gmail.com");
        var modificado = estudianteDao.modificarEstudiante(estudiantesModificados);
        if (modificado)
            System.out.println("Estudiante modificado: "+estudiantesModificados);
        else
            System.out.println("No se modifico estudainte: "+estudiantesModificados);


        //agregar estudiante
        //var nuevoEstudiante = new Estudiante("Carlos", "Lara", "2614535678", "Larilugg@gmail.com");
        //var agregado = estudianteDao.agregarEstudiante(nuevoEstudiante);
        //if (agregado)
        //7  System.out.println("Estudiante agregado: "+nuevoEstudiante);
        //else
        //  System.out.println("No se ha agregado estudiante:  "+nuevoEstudiante);



        //Eliminar estudiante con id 3
        var estudianteEliminar = new Estudiante(3);
        var eliminado = estudianteDao.eliminarEstudiante(estudianteEliminar);
        if (eliminado)
            System.out.println("ESTUDIANTE ELIMINADO: "+estudianteEliminar);
        else
            System.out.println("No se elimnino estudiante: "+estudianteEliminar);


        //Listar estudiantes

        System.out.println("Listado de estudiantes: ");
        List<Estudiante> estudiantes = estudianteDao.listarEstudiantes();
        estudiantes.forEach(System.out::println); //Impresion




        //Buscar por id
       // var estudiante1 = new Estudiante(1);
        //System.out.println("Estudiantes antes de la busqyeda: "+estudiante1);
        //var encontrado = estudianteDao.buscarEstudiantesPorId(estudiante1);
       // if (encontrado)
          //  System.out.println("Estudiante encontrado: "+estudiante1);
        //else
            //System.out.println("No se encontró el estudiante: "+estudiante1.getIdEstudiante());

    }
}
