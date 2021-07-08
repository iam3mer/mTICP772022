package utp.misiontic2022.c2.p77.ejercicios;

public class App 
{
    public static void main( String[] args )
    {
        Nota nota = new Nota();

        nota.setEscala100(80);
        nota.setEscala5(4.0);
        nota.setEscalaCualitativa("Sobresaliente");

        System.out.println(nota.getEscalaCualitativa());
        nota.mostrarEscala();

        Asignatura asig1 = new Asignatura("Programación",4,80,90,65,70,70);
        asig1.mostrarPromedio();
    }
}
