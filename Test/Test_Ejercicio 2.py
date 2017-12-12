import unittest
import Ejercicio_2

class Ejercicio2test(unittest.TestCase):

    def testdevuelveCoordenadasDeBarcosNoHundidosRecibeMapaVaciaDeberiaDevolverUnaListaVacia(self):
        # Arrange
        mapaVacio = []
        # Act
        resultado = Ejercicio_2.devuelveCoordenadasDeBarcosNoHundidos(mapaVacio)
        # Assert
        self.assertTrue(resultado == [])