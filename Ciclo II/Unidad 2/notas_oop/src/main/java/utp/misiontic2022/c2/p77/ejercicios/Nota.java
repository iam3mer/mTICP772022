package utp.misiontic2022.c2.p77.ejercicios;

public class Nota {

    // Atributos
    private Integer escala100;
    private Double escala5;
    private String escalaCualitativa;

    // Constructores
    public Nota () {
        this.escala100 = 0;
        this.escala5 = 0.0;
        this.escalaCualitativa = "";
    }

    public Nota (Integer pEscala100) {
        this.escala100 = pEscala100;
        this.escala5 = pEscala100 * 0.05;
        if (pEscala100 >= 0 & pEscala100 <= 20) {
            this.escalaCualitativa = "Deficiente";
        } else if (pEscala100 >= 21 & pEscala100 <= 59) {
            this.escalaCualitativa = "Insuficiente";
        } else if (pEscala100 >= 60 & pEscala100 <= 79) {
            this.escalaCualitativa = "Aceptable";
        } else if (pEscala100 >= 80 & pEscala100 <= 96) {
            this.escalaCualitativa = "Sobresaliente";
        } else {
            this.escalaCualitativa = "Excelente";
        }
    }

    public Nota (Double pEscala5) {
        this.escala100 = (int)(pEscala5 * 20);
        this.escala5 = pEscala5;
        if (pEscala5 >= 0 & pEscala5 <= 1) {
            this.escalaCualitativa = "Deficiente";
        } else if (pEscala5 >= 1.1 & pEscala5 <= 2.9) {
            this.escalaCualitativa = "Insuficiente";
        } else if (pEscala5 >= 3.0 & pEscala5 <= 3.9) {
            this.escalaCualitativa = "Aceptable";
        } else if (pEscala5 >= 4.0 & pEscala5 <= 4.8) {
            this.escalaCualitativa = "Sobresaliente";
        } else {
            this.escalaCualitativa = "Excelente";
        }
    }

    // Metodos
    public void mostrarEscala () {
        System.out.println("------EscalaNota------");
        System.out.printf("Nota en escala 100: %d\n", getEscala100());
        System.out.printf("Nota en escala 5: %.2f\n", getEscala5());
        System.out.printf("Nota en escala cualitativa: %s\n", this.escalaCualitativa);
    }

    public Integer getEscala100() {
        return escala100;
    }

    public void setEscala100(Integer escala100) {
        this.escala100 = escala100;
    }

    public Double getEscala5() {
        return escala5;
    }

    public void setEscala5(Double escala5) {
        this.escala5 = escala5;
    }

    public String getEscalaCualitativa() {
        return escalaCualitativa;
    }

    public void setEscalaCualitativa(String escalaCualitativa) {
        this.escalaCualitativa = escalaCualitativa;
    }

    
    
}
