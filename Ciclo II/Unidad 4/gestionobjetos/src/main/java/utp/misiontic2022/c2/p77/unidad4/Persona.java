package utp.misiontic2022.c2.p77.unidad4;

import java.io.Serializable;

public class Persona implements Serializable {
    private String first_name;
    private String last_name;
    private Integer nuip;
    private String city;

    public Persona(String first_name, String last_name, Integer nuip, String city) {
        this.first_name = first_name;
        this.last_name = last_name;
        this.nuip = nuip;
        this.city = city;
    }

    @Override
    public String toString() {
        return getNuip()+" "+getFirst_name()+" "+getLast_name();
    }

    public String getFirst_name() {
        return first_name;
    }

    public void setFirst_name(String first_name) {
        this.first_name = first_name;
    }

    public String getLast_name() {
        return last_name;
    }

    public void setLast_name(String last_name) {
        this.last_name = last_name;
    }

    public Integer getNuip() {
        return nuip;
    }

    public void setNuip(Integer nuip) {
        this.nuip = nuip;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    
}
