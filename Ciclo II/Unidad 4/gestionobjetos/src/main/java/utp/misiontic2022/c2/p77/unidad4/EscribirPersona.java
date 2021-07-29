package utp.misiontic2022.c2.p77.unidad4;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.util.List;

public class EscribirPersona {

    public static void writePeople(String nomFile, List<Persona> people) {
        try {
            //String nomFile = "personas.data";
            FileOutputStream file = new FileOutputStream(nomFile);
            ObjectOutputStream oos = new ObjectOutputStream(file);
    
            for (Persona persona : people) {
                    oos.writeObject(persona);
            }
            
            oos.close();
        } catch (FileNotFoundException e) {
            System.err.println("El archivo no existe!");
        } catch (IOException e) {
            System.err.println(e.getMessage());
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }
    }
}
