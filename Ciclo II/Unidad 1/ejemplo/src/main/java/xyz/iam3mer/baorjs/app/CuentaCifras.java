package xyz.iam3mer.baorjs.app;

import java.util.Scanner;

public class CuentaCifras {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Ingrese un numero: ");
        int numero = input.nextInt();

        int cantidadCifras = cuentaCifras(numero);

        System.out.printf("El numero %d tiene %d cifra(s)", numero, cantidadCifras);

        input.close();
    }

    public static int cuentaCifras(int numero) {
        int cifras = numero == 0 ? 1 : 0;

        while (numero != 0) {
            numero /= 10;
            cifras++;
        }

        return cifras;
    }
}
