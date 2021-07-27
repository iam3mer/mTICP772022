package utp.misiontic2022.c2.p77.unidad4;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

public class EscribirPersona {
    public static void writePeople() {
        try {
            String nomFile = "personas.data";
            FileOutputStream file = new FileOutputStream(nomFile);
            ObjectOutputStream oos = new ObjectOutputStream(file);
    
            oos.writeObject(new Persona("Jhonatan", "Barrera", 23452342, "Pereira"));
            oos.writeObject(new Persona("Maria", "Carvajal", 335344, "Manizales"));
            oos.writeObject(new Persona("Harold", "Sequeda", 456787, "Bogota"));
            oos.writeObject(new Persona("Cesar", "Moreno", 56567445, "Medellin"));
            
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
