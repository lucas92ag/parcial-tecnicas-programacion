import unittest
import Ejercicio_1

class Ejercicio1test(unittest.TestCase):

    def testRotaCaracteresDeUnaPalabraRecibeCadenaVaciaDeberiaDevolverUnaListaVacia(self):
        # Arrange
        cadenaVacia = ''
        # Act
        resultado = Ejercicio_1.rotaCaracteresDeUnaPalabra(cadenaVacia)
        # Assert
        self.assertTrue(resultado == [])

    def testRotaCaracteresDeUnaPalabraRecibeCadenaDeEspaciosDeveriaDevolverListaVacia(self):
        # Arrange
        cadenaDeEspacios = '     '
        # Act
        result = Ejercicio_1.rotaCaracteresDeUnaPalabra(cadenaDeEspacios)
        # Assert
        self.assertTrue(result == [])

    def testRotaCaracteresDeUnaPalabraRecibeUnaLetraDeveriaDevolverListaConMismaLetra(self):
        # Arrange
        cadena = 'a'
        # Act
        result = Ejercicio_1.rotaCaracteresDeUnaPalabra(cadena)
        # Assert
        self.assertTrue(result == ['a'])

    def testRotaCaracteresDeUnaPalabraRecibeCadenaDeDosCaracteresDeberiaDevolverListaConDosRotaciones(self):
        # Arrange
        cadena = 'ab'
        # Act
        result = Ejercicio_1.rotaCaracteresDeUnaPalabra(cadena)
        # Assert
        self.assertTrue(result == ['ab','ba'])

    def testRotaCaracteresDeUnaPalabraRecibeCadenaDeTresCaracteresDeberiaDevolverListaConTresSusRotaciones(self):
        # Arrange
        cadena = 'paz'
        # Act
        result = Ejercicio_1.rotaCaracteresDeUnaPalabra(cadena)
        # Assert
        self.assertTrue(result == ['paz','azp','zpa'])

    def testRotaCaracteresDeUnaPalabraRecibeCadenaDeDosCaracteresUnEspacioYUnCaracterDeberiaDevolverListaCon4Rotaciones(self):
        # Arrange
        cadena = 'so l'
        # Act
        result = Ejercicio_1.rotaCaracteresDeUnaPalabra(cadena)
        # Assert
        self.assertTrue(result == ['so l','o ls',' lso','lso '])

    def testRotaCaracteresDeUnaPalabraRecibeCadenaDeCincoCaracteresDeberiaDevolverListaCon5Rotaciones(self):
        # Arrange
        cadena = 'rotar'
        # Act
        result = Ejercicio_1.rotaCaracteresDeUnaPalabra(cadena)
        # Assert
        self.assertTrue(result == ['rotar','otarr','tarro','arrot','rrota'])