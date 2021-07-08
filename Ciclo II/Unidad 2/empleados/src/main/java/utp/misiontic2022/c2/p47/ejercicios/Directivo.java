package utp.misiontic2022.c2.p47.ejercicios;

public final class Directivo extends Empleado {
    // Atributos
    private String categoria;
    
    // Constructor
    public Directivo (String pNombre, Integer pEdad, Double pSueldoBruto,
                    Double pPagoSalud, Double pPagoPension, String pCategoria) {
                        super(pNombre, pEdad, pSueldoBruto, pPagoSalud, pPagoPension);
                        this.categoria = pCategoria;
                    }

    // Metodos
    @Override
    public void mostrar() {
        System.out.println(this.categoria);
    }
}
