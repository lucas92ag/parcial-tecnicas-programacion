import unittest
import Ejercicio_2

class Ejercicio2test(unittest.TestCase):



    def testdevuelveCoordenadasDeBarcosNoHundidosRecibeMapaVaciaDeberiaDevolverUnaListaVacia(self):
        # Arrange
        mapaVacio = []
        disparos = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = Ejercicio_2.devuelveCoordenadasDeBarcosNoHundidos(mapaVacio, disparos)
        # Assert
        self.assertTrue(resultado == [])

    def testDevuelveCoordenadasDeBarcosNoHundidosRecibeStrinVacioDeberiaDevolverUnaListaVacia(self):
        # Arrange
        stringVacio = ""
        disparos = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = Ejercicio_2.devuelveCoordenadasDeBarcosNoHundidos(stringVacio, disparos)
        # Assert
        self.assertTrue(resultado == [])

    def testDevuelveCoordenadasDeBarcosNoHundidosRecibeCadenaSoloConEspaciosDeberiaDevolverUnaListaVacia(self):
        # Arrange
        cadenaDeEspacios = "      "
        disparos = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = Ejercicio_2.devuelveCoordenadasDeBarcosNoHundidos(cadenaDeEspacios, disparos)
        # Assert
        self.assertTrue(resultado == [])

    def testdevuelveCoordenadasDeBarcosNoHundidosRecibeListaConCadenaDeCaracteresDiferentesDePuntoOBLargaDeberiaDevolverListaVacia(self):
        # Arrange
        cadenaInvalida = "soy NO valido"
        disparos = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = Ejercicio_2.devuelveCoordenadasDeBarcosNoHundidos(cadenaInvalida, disparos)
        # Assert
        self.assertTrue(resultado == [])