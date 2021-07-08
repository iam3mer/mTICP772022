package utp.misiontic2022.c2.p47.ejercicios;

public final class Cliente extends Persona {
    // Atributos
    private String telefono;

    // Constructor
    public Cliente(String pNombre, Integer pEdad, String pTelefono) {
        super(pNombre, pEdad);
        this.telefono = pTelefono;
    }

    // Metodos
    public void mostrar() {
        System.out.println(this.telefono);
    }
    
}
