package utp.misiontic2022.c2.p77.unidad4;

import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;

public class LeerPersona {
    private Integer suma = 0;

    public void readPeople() {
        final String NOM_FILE = "personas.data";

        try (
            FileInputStream file = new FileInputStream(NOM_FILE);
            ObjectInputStream ois = new ObjectInputStream(file);
        ) {

            Persona persona = (Persona) ois.readObject();
            
            while (persona != null) {
                if (persona instanceof Persona) {
                    System.out.println(persona);

                    setSuma(getSuma() + persona.getNuip());
                    //this.suma = this.suma + persona.getNuip();
                }

                persona = (Persona) ois.readObject();
            }

        } catch (EOFException e) {
        } catch (IOException e) {
            System.err.println(e.getMessage());
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }
    }

    public Integer getSuma() {
        return suma;
    }

    public void setSuma(Integer suma) {
        this.suma = suma;
    }
}
