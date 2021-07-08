package utp.misiontic2022.c2.p77.ejercicios;

public class Asignatura {
    // Atributos
    private String nomAsignatura;
    private Integer numCredito;
    private Nota nota1;
    private Nota nota2;
    private Nota nota3;
    private Nota nota4;
    private Nota nota5;
    private Integer promedio100;
    private Nota peorNota;
    
    // Constructores
    public Asignatura() {
        setNomAsignatura("nomAsignatura");
        setNumCredito(0);
        setNota1(new Nota());
        setNota2(new Nota());
        setNota3(new Nota());
        setNota4(new Nota());
        setNota5(new Nota());
    }

    public Asignatura(String pNombreAsignatura, Integer pNumCredito, Integer pNota1_100,
                Integer pNota2_100, Integer pNota3_100, Integer pNota4_100,
                Integer pNota5_100) {
                    setNomAsignatura(pNombreAsignatura);
                    setNumCredito(pNumCredito);
                    setNota1(new Nota(pNota1_100));
                    setNota2(new Nota(pNota2_100));
                    setNota3(new Nota(pNota3_100));
                    setNota4(new Nota(pNota4_100));
                    setNota5(new Nota(pNota5_100));
                }

    // Metodos
    public void mostrarPromedio() {
        this.calcularPromedio();
        System.out.println("------Promedio------");
        System.out.println("Nombre de la asignatura: " + getNomAsignatura());
        Nota auxPromedio = new Nota(promedio100);
        auxPromedio.mostrarEscala();
    }

    public void encontrarPeorNota() {
        setPeorNota(nota1);

        if (nota2.getEscala100() < peorNota.getEscala100()) {
            setPeorNota(nota2);
        }

        if (nota3.getEscala100() < peorNota.getEscala100()) {
            setPeorNota(nota3);
        }

        if (nota4.getEscala100() < peorNota.getEscala100()) {
            setPeorNota(nota4);
        }

        if (nota5.getEscala100() < peorNota.getEscala100()) {
            setPeorNota(nota5);
        }
    }

    public void calcularPromedio() {
        this.encontrarPeorNota();

        this.promedio100 = (nota1.getEscala100() + nota2.getEscala100()
                        + nota3.getEscala100() + nota4.getEscala100()
                        + nota5.getEscala100() - peorNota.getEscala100()) / 4;
    }

    public String getNomAsignatura() {
        return nomAsignatura;
    }

    public void setNomAsignatura(String nomAsignatura) {
        this.nomAsignatura = nomAsignatura;
    }

    public Integer getNumCredito() {
        return numCredito;
    }

    public void setNumCredito(Integer numCredito) {
        this.numCredito = numCredito;
    }

    public Nota getNota1() {
        return nota1;
    }

    public void setNota1(Nota nota1) {
        this.nota1 = nota1;
    }

    public Nota getNota2() {
        return nota2;
    }

    public void setNota2(Nota nota2) {
        this.nota2 = nota2;
    }

    public Nota getNota3() {
        return nota3;
    }

    public void setNota3(Nota nota3) {
        this.nota3 = nota3;
    }

    public Nota getNota4() {
        return nota4;
    }

    public void setNota4(Nota nota4) {
        this.nota4 = nota4;
    }

    public Nota getNota5() {
        return nota5;
    }

    public void setNota5(Nota nota5) {
        this.nota5 = nota5;
    }

    public Nota getPeorNota() {
        return peorNota;
    }

    public void setPeorNota(Nota peorNota) {
        this.peorNota = peorNota;
    }

    

}
