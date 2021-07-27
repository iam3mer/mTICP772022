package utp.misiontic2022.c2.p77.unidad4;

import java.io.FileNotFoundException;

//import java.io.File;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args ) throws FileNotFoundException
    {
        /*
        String nomFile = "archivo.txt";
        var file = new File(nomFile);

        System.out.println(file.getName()); // Nombre del archivo
        System.out.println(file.getAbsolutePath()); // Ruta absoluta
        System.out.println(file.getParent());
        System.out.println(file.isFile());
        System.out.println(file.exists());

        if (!file.exists()) {
            System.out.println("El archivo no existe!");
        }
        */

        EscribirArchivo.write();
        LeerArchivo.read();
    }
}
