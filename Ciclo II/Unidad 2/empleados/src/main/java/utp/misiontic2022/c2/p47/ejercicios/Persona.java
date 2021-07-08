package utp.misiontic2022.c2.p47.ejercicios;

public abstract class Persona {
    // Atributos
    private String nompre;
    private Integer edad;

    // Constructor
    public Persona (String pNombre, Integer pEdad) {
        this.nompre = pNombre;
        this.edad = pEdad;
    }
    

    // Metodos
    /*
    public void mostrar() {
        System.out.println(this.nompre);
        System.out.println(this.edad);
    }
    */

    public abstract void mostrar();

}
