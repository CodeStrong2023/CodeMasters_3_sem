
package Enumeraciones;

public enum Continentes {
    AFRICA(54,"1.3 billones"),
    EUROPA(50,"741 millones"),
    AMERICA(35, "1 billon"),
    ASIA(48, "4.7 billones"), // SE PUEDE USAR , O ;
    OCEANIA(14,"43 millones"); 
    
    private final int paises;
    private String habitantes;
    
    Continentes(int paises, String habitantes){
        this.paises = paises;
        this.habitantes = habitantes;
    }
    
    public int getPaises(){
        return this.paises;
    }
    
    public String getHabitantes(){
       return this.habitantes;
    }
}
