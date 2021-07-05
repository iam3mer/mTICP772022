package xyz.iam3mer.ejerciciosp77.baorjs;

import java.util.Scanner;

public class Ejercicio7 {

    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);

        System.out.println("Ingrese el caracter: ");

        char letra = input.nextLine().charAt(0);

        input.close();

        if (Character.isUpperCase(letra)){
            System.out.printf("%c es una letra mayuscula.", letra);
        }

    }
    
}
