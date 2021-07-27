package utp.misiontic2022.c2.p77.unidad4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;

public class IO_3 {
    public static void run() {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter output = new PrintWriter(System.out, true);

        String line = null;

        output.println("Escriba una linea de texto");
        try {
            line = input.readLine();
        } catch (IOException e) {
            System.err.println(e);
        }
        output.println("La linea escrita es: ");
        output.println(line);
    }
}
