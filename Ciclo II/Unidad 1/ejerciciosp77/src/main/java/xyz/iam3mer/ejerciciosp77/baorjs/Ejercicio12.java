package xyz.iam3mer.ejerciciosp77.baorjs;

import java.security.ProtectionDomain;
import java.util.Scanner;

public class Ejercicio12 {
    public static void main(String[] args) {
        Integer limite = 100;
        Integer residuo = 0;
        
        System.out.println("for");
        for (int i = 1; i <= limite; i++) {
            residuo = i % 3;
            if (residuo!=0) {
                System.out.printf("%d ", i);
            }
        }

        System.out.printf("\nwhile\n");
        Integer i = 1;
        while (i <= limite) {
            residuo = i % 3;
            if (residuo!=0) {
                System.out.printf("%d ", i);
            }
            i++;
        }

        System.out.printf("\ndo-while\n");
        i = 1;
        do {
            residuo = i % 3;
            if (residuo!=0) {
                System.out.printf("%d ", i);
            }
            i++;
        } while (i <= limite);

    }
}
