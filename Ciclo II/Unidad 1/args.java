import java.util.Scanner;

/**
 * Hello world!
 *
 */
public class args 
{
    public static void main( String[] args ) 
    {   
        Scanner input = new Scanner(System.in);

        System.out.println( "Ingrese su nombre: " );
        String nombre = input.nextLine();

        input.close();

        System.out.printf("Hola %s %S\n", nombre, args[0]);
    }
}