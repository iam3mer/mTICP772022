package xyz.iam3mer.ejerciciosp77.baorjs;

import java.util.Scanner;

public class Ejercicio10 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Ingrese el valor para H: ");
        Integer H = input.nextInt();
        System.out.println("Ingrese el valor para M: ");
        Integer M = input.nextInt();
        System.out.println("Ingrese el valor para S: ");
        Integer S = input.nextInt();
        
        if (H < 0 || H > 23) {
            System.out.printf("La hora no es valida. %d no hace parte del dominio de H\n", H);
        }

        if (M < 0 || M > 59) {
            System.out.printf("La hora no es valida. %d no hace parte del dominio de M\n", M);
        }

        if (S < 0 || S > 59) {
            System.out.printf("La hora no es valida. %d no hace parte del dominio de S\n", S);
        }
    }
}
