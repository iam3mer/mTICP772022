package utp.misiontic2022.c2.p77.unidad4;

import java.io.FileNotFoundException;
import java.io.PrintWriter;

public class EscribirArchivo {
    public static void write () throws FileNotFoundException {
        int[][] num = {{234,234,234,234,234},
                        {68534,534,534,534},
                        {345,3456,4576,47,567}};

        String nomFile = "numFile.txt";

        PrintWriter output = new PrintWriter(nomFile);

        for (int i = 0; i < num.length; i++) {
            for (int j = 0; j < num.length; j++) {
                output.print(num[i][j] + ",");
            }
            output.println();
        }
        output.close();
    }
}
