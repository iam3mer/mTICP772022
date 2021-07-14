package utp.misiontic2022.c2.p77.ejercicios;

/**
 * Hello world!
 *
 */
public class App 
{
    private static Integer integer;

    public static void main( String[] args )
    {
        try{
            System.out.println(8/0);
        } catch (ArithmeticException exception) {
            // Gestion de la excepción
            System.out.println("No se puede dividir entre cero " + exception);
        } finally {
            System.out.println("Este es el finally. Siempre se ejecuta es bloque.");
        }

        try {
        Integer[] num = new Integer[5];
        num[0] = 5;
        integer = num[0];
        } catch (Exception | Error ex) {
            System.out.println("Algo pasa con el array definido");
        }
    }
}
