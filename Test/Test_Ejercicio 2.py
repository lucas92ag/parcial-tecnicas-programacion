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

    def testDevuelveCoordenadasDeBarcosNoHundidosRecibeListaConCadenaDeCaracteresDiferentesDePuntoOBLargaDeberiaDevolverListaVacia(self):
        # Arrange
        cadenaInvalida = "soy NO valido"
        disparos = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = Ejercicio_2.devuelveCoordenadasDeBarcosNoHundidos(cadenaInvalida, disparos)
        # Assert
        self.assertTrue(resultado == [])

    def testDevuelveCoordenadasDeBarcosNoHundidosRecibeListaConCadenasDeCaracteresDiferentesDePuntoOBLargaDeberiaDevolverListaVacia(self):
        # Arrange
        listaDeCadenasInvalidas = ["yo","tambien","soy","invalido"]
        disparos = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = Ejercicio_2.devuelveCoordenadasDeBarcosNoHundidos(listaDeCadenasInvalidas, disparos)
        # Assert
        self.assertTrue(resultado == [])

    def testDevuelveCoordenadasDeBarcosNoHundidosRecibeListaConCadenasDeDiferentesLenghtDeberiaDevolverListaVacia(self):
        # Arrange
        listaDeCadenasConDistintoLenght = ["b.b.","....","..bb","b.b"]
        disparos = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = Ejercicio_2.devuelveCoordenadasDeBarcosNoHundidos(listaDeCadenasConDistintoLenght, disparos)
        # Assert
        self.assertTrue(resultado == [])

    def testDevuelveCoordenadasDeBarcosNoHundidosRecibeUnMapaValidoDeberiaDevolverListaConBarcosIntactos(self):
        # Arrange
        mapaValido = ["b.b..","b...b",".....","....b"]
        disparos = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = Ejercicio_2.devuelveCoordenadasDeBarcosNoHundidos(mapaValido, disparos)
        # Assert
        self.assertTrue(resultado == [(2, 1), (2, 5)])

    def testDevuelveCoordenadasBarcosNoHundidosRecibeUnMapaValidoYUnaListaDeDisparosVaciaDeberiaDevolverListaConBarcosIntactos(self):
        # Arrange
        mapaValido = ["b..","...","..b"]
        listaDeDisparosVacia = []
        # Act
        resultado = Ejercicio_2.devuelveCoordenadasDeBarcosNoHundidos(mapaValido, listaDeDisparosVacia)
        # Assert
        self.assertTrue(resultado == [(1, 1), (3, 3)])