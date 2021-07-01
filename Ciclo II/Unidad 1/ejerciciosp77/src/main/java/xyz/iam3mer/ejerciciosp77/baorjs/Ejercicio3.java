package xyz.iam3mer.ejerciciosp77.baorjs;

import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Ingrese el numero N: ");
        Integer N = input.nextInt();

        System.out.println("Ingrese el numero m: ");
        Integer m = input.nextInt();

        input.close();

        Integer cifras = cuentaCifras(N);

        System.out.println(cifras);

        
        if (cifras < m) {
            System.out.println("No queda nada a mostrar.");
        }

        else if (cifras >= m) {
                Integer cont = 0;
                Integer auxN = N;
                while (cont < m) {
                    auxN /= 10;
                    ++cont;
                }
                System.out.printf("Valor inicial(N): %d\nValor de m: %d\nValor final: %d",
                N, m, auxN);
        } 
        
    }

    public static Integer cuentaCifras(int numero) {
        Integer cifras = numero == 0 ? 1 : 0;

        while (numero != 0) {
            numero /= 10;
            cifras++;
        }

        return cifras;
    }
}
