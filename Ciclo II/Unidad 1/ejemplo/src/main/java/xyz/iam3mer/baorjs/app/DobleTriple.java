package xyz.iam3mer.baorjs.app;

import java.util.Scanner;

public class DobleTriple {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Ingrese un numero: ");
        int numero = input.nextInt();

        int[] respuesta = auxCalculo(numero);

        System.out.printf("El doble es %d y el triple es %d", respuesta[0], respuesta[1]);

        input.close();
    }

    public static int[] auxCalculo(int numero) {
        int doble = numero * 2;
        int triple = numero * 3;

        return new int[] {doble, triple};
    }
}
