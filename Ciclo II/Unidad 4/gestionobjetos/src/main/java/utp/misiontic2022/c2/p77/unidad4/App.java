package utp.misiontic2022.c2.p77.unidad4;

import java.util.Arrays;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        EscribirPersona.writePeople(
            "personas.data", 
            Arrays.asList(
                new Persona("Jhonatan", "Barrera", 24245, "Pereira"),
                new Persona("Maria", "Carvajal", 5757, "Manizales"),
                new Persona("Harold", "Sequeda", 7257, "Bogota"),
                new Persona("Cesar", "Moreno", 24778, "Medellin")
            )
            );
        
        LeerPersona personas = new LeerPersona();
        personas.readPeople();
        System.out.printf("La suma de las identificaciones es: %d\n", personas.getSuma());
    }
}
