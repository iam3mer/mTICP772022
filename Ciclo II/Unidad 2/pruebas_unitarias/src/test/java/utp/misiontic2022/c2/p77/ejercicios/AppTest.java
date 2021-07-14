package utp.misiontic2022.c2.p77.ejercicios;

import static org.junit.Assert.assertTrue;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.Test;

/**
 * Unit test for simple App.
 */
public class AppTest 
{
    /**
     * Rigorous Test :-)
     */
    @Test
    void suma2Numeros() {
        App sumar = new App();
        assertEquals(8, sumar.sumar(5, 3));
    }
}
