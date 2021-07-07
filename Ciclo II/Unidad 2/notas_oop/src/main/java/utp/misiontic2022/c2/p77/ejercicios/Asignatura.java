package utp.misiontic2022.c2.p77.ejercicios;

public class Asignatura {
    // Atributos
    private String nomMateria;
    private Integer numCredito;
    private Nota nota1;
    private Nota nota2;
    private Nota nota3;
    private Nota nota4;
    private Nota nota5;
    
    // Constructores
    public Asignatura() {
        setNomMateria("nomMateria");
        setNumCredito(0);
        setNota1(new Nota());
        setNota2(new Nota());
        setNota3(new Nota());
        setNota4(new Nota());
        setNota5(new Nota());
    }

    // Metodos
    public String getNomMateria() {
        return nomMateria;
    }
    public void setNomMateria(String nomMateria) {
        this.nomMateria = nomMateria;
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
}
