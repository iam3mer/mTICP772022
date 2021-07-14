package utp.misintic2022.c2.p77.ejercicios;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;


/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        //listas();
        //conjuntos();
        mapas();
    }

    public static void listas () {

        System.out.println("Lista de Objetos");
        List<Object> lista = new ArrayList<>(); // Object: Permite que se guarde en la lista cualquier tipo de objeto

        ObjetoDemo myObject = new ObjetoDemo();

        lista.add(5);
        lista.add(8.0);
        lista.add(myObject);

        //System.out.println(myObject.toString());

        for (int i = 0; i < lista.size(); i++) {
            System.out.println(lista.get(i));
        }

        lista.add(1, "element");

        System.out.println("--------------");

        // Foreach
        for (Object object : lista) {
            System.out.println(object);
        }

        System.out.println("Lista de Enteros");

        List<Integer> listaEnteros = new ArrayList<Integer>();

        listaEnteros.add(8);
        listaEnteros.add(5);
        listaEnteros.add(43);
        listaEnteros.add(2);

        System.out.println(listaEnteros.contains(43));

        //listaEnteros.forEach((entero) -> System.out.println(entero));

        Iterator<Integer> iterador = listaEnteros.iterator();
        while(iterador.hasNext()){
            Integer entero = iterador.next();
            System.out.println(entero);
        }
    }

    public static void conjuntos () {
        Set<Integer> conjuntoEnteros = new LinkedHashSet<>();

        conjuntoEnteros.add(5);
        conjuntoEnteros.add(78);
        conjuntoEnteros.add(6);
        conjuntoEnteros.add(6);
        conjuntoEnteros.add(45);

        System.out.println(conjuntoEnteros);

        System.out.println(conjuntoEnteros.size());
        System.out.println(conjuntoEnteros.contains(5));
        conjuntoEnteros.remove(6);

        System.out.println(conjuntoEnteros);

        for (Integer num: conjuntoEnteros) {
            System.out.println(num);
        }
    }


    public static void mapas() {
        Map<String, Object> mapa = new HashMap<>();

        ObjetoDemo myObject = new ObjetoDemo();

        mapa.put("Calificación", 5);
        mapa.put("Estudiante", "Jhonatan");
        mapa.put("Asignatura", "Programación");
        mapa.put("Objeto", myObject);

        System.out.println(mapa.containsKey("Estudiante"));
        System.out.println(mapa.containsValue(7));

        mapa.remove("Objeto");

        Set<String> llaves = mapa.keySet();

        for (String llave : llaves) {
            System.out.println(llave);
        }

        Collection<Object> valores = mapa.values();

        for (Object valor : valores) {
            System.out.println(valor);
        }
    }
}
