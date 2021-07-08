package utp.misiontic2022.c2.p47.ejercicios;

public class Empleado extends Persona {
    // Atributos
    private Double sueldoBruto;
    private Double sueldoNeto;
    private Double pagoSalud;
    private Double pagoPension;

    // Constructores
    public Empleado(String pNombre, Integer pEdad, Double pSueldoBruto,
                    Double pPagoSalud, Double pPagoPension) {
        super(pNombre, pEdad);
        this.sueldoBruto = pSueldoBruto;
        this.pagoSalud = pPagoSalud;
        this.pagoPension = pPagoPension;
    }

    // Metodos
    public void mostrar() {
        System.out.println("------InfoEmpleado------");
        System.out.println(this.sueldoBruto);
        System.out.println(this.sueldoNeto);
    }

    public void calcularSalarioNeto(){
        this.sueldoNeto = this.sueldoBruto - this.pagoSalud - this.pagoPension;
    }
}
