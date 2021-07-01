package xyz.iam3mer.baorjs.app;

import java.util.Scanner;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args ) 
    {   
        Scanner input = new Scanner(System.in);

        System.out.println( "Ingrese un numero: " );
        int numero = input.nextInt();

        System.out.println("Ejemplo de if");

        if (numero == 17) {
            System.out.println("Estas en el grupo 17.");
        }
        
        else if (numero == 47) {
            System.out.println("Estas en el grupo 47.");
        }

        else if (numero == 77) {
            System.out.println("Estas en el grupo 77.");
        }

        else {
            System.out.printf("Estas en el grupo %d\n", numero);
        }

        System.out.println("Ejemplo de switch");

        switch (numero) {
            case 17:
                System.out.println("Estas en el grupo 17.");
                break;
            case 47:
                System.out.println("Estas en el grupo 47.");
                break;
            case 77:
                System.out.println("Estas en el grupo 77.");
                break;
            default:
                System.out.printf("Estas en el grupo %d\n", numero);
                break;
        }

        System.out.println("Ejemplo de while");

        boolean band = true;
        int contador = 0;

        while (band) {

            contador += 1;

            if (contador > 4) {
                band = false;
            }

            System.out.println( "Ingrese un numero: " );
            numero = input.nextInt();

            switch (numero) {
                case 17:
                    System.out.println("Estas en el grupo 17.");
                    break;
                case 47:
                    System.out.println("Estas en el grupo 47.");
                    break;
                case 77:
                    System.out.println("Estas en el grupo 77.");
                    break;
                default:
                    System.out.printf("Estas en el grupo %d\n", numero);
                    break;
            }
        }

        System.out.println("Ejemplo de do-while");

        band = false;

        do {
            //contador += 1;
            ++contador;

            if (contador > 4) {
                band = false;
            }

            System.out.println( "Ingrese un numero: " );
            numero = input.nextInt();

            switch (numero) {
                case 17:
                    System.out.println("Estas en el grupo 17.");
                    break;
                case 47:
                    System.out.println("Estas en el grupo 47.");
                    break;
                case 77:
                    System.out.println("Estas en el grupo 77.");
                    break;
                default:
                    System.out.printf("Estas en el grupo %d\n", numero);
                    break;
            }
        } while (band);

        System.out.println("Ejemplo for");

        for (int i=0; i<4; i++) {
            System.out.println( "Ingrese un numero: " );
            numero = input.nextInt();

            if (numero == 17) {
                System.out.println("Estas en el grupo 17.");
            }
            
            else if (numero == 47) {
                System.out.println("Estas en el grupo 47.");
            }
    
            else if (numero == 77) {
                System.out.println("Estas en el grupo 77.");
            }
    
            else {
                System.out.printf("Estas en el grupo %d\n", numero);
            }
        }

        input.close();
    }
}
