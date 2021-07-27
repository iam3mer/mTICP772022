package utp.misiontic2022.c2.p77.unidad4;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.util.StringTokenizer;

public class LeerArchivo {
    public static void read () {
        String nomFile = "numFile.txt";

    File file = new File(nomFile);

    if (file.exists()) {
        try {
            Scanner input = new Scanner(file);

            while (input.hasNext()) {
                StringTokenizer num = new StringTokenizer(input.next(), ",");
                while (num.hasMoreTokens()) {
                    System.out.print(num.nextToken() + "\t");
                }
                System.out.println();
            }

            input.close();
        } catch (IOException e) {
            System.err.println(e);
        }

    } else {
        System.out.println("El fichero no existe!");
    }
    }
}
