package xyz.iam3mer.baorjs.app;

import java.util.Scanner;

public class NumeroSuerte {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.println("Ingrese una fecha: "); // 12/07/1980
        String fecha = input.nextLine();

        input.close();

        int indiceSeparador1 = fecha.indexOf('/');

        int dia = Integer.parseInt(fecha.substring(0, indiceSeparador1));

        System.out.println(dia);



    }
}
