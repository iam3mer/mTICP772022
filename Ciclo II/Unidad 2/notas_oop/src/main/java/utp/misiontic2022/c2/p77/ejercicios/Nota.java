package utp.misiontic2022.c2.p77.ejercicios;

public class Nota {

    // Atributos
    public Integer escala100;
    public Double escala5;
    public String escalaCualitativa;

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
    
}
