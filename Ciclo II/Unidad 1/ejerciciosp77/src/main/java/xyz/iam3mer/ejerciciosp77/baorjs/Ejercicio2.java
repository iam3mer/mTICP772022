package xyz.iam3mer.ejerciciosp77.baorjs;

import java.util.Scanner;

/**
 * Hello world!
 *
 */
public class Ejercicio2 
{
    public static void main( String[] args )
    {
        Scanner input = new Scanner(System.in);

        System.out.println( "Ingrese el precio sin iva del producto: " );
        Integer precio = input.nextInt();
        System.out.println( "Ingrese la cantidad a comprar: " );
        Integer cantidad = input.nextInt();
        System.out.println( "Ingrese el iva a aplicar: " );
        Integer iva = input.nextInt();

        input.close();

        Integer precioIva = precio + (precio * iva / 100);

        Integer total = precioIva * cantidad;

        System.out.printf("El valor total de la compra es: %d", total);
    }
}
