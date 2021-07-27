package utp.misiontic2022.c2.p77.unidad4;

import java.io.IOException;

public class IO_1 {
    public static void run() {
        int numBytes = 0;
        char character;

        System.out.println("Escriba un texto: ");

        try {
            do {
                character = (char) System.in.read();
                System.out.print(character);
                numBytes++;
            } while (character != '\n'); //\r\n
            System.out.printf("%d bytes leidos \n", numBytes);
        } catch (IOException e) {
            System.err.println(e);
        }
    }
}
