package utp.misiontic2022.c2.p77.ejercicios;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        Double auxNota = Double.parseDouble(args[1]);
        Double promedio = auxNota;

        for (int i = 2; i < args.length; i++) {
            promedio += Double.parseDouble(args[i]);
            if (Double.parseDouble(args[i]) < auxNota) {
                auxNota = Double.parseDouble(args[i]);
            }
        }

        promedio -= auxNota;
        promedio /= 4;
        promedio *= 0.05;

        System.out.printf("El promedio del estudiantes con id %s es: %.2f",
                        args[0], promedio);

    }
}
