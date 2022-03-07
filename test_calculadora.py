import unittest
from calculadora import Calculadora

class PruebaCalculadora(unittest.TestCase):

    def setUp(self):
        # Configurar la prueba al INICIO de cada prueba (una vez por prueba)
        self.calculadora = Calculadora()

    def test_suma(self):
        resultado = self.calculadora.suma(2, 4, 3)
        self.assertEqual(resultado, 9)

    def test_resta(self):
        resultado = self.calculadora.resta(4, 2)
        self.assertEqual(resultado, 2)
    
    
    def test_multiplicacion(self):
        resultado = self.calculadora.multiplicacion(2, 4)
        self.assertEqual(resultado, 8)
    
    def test_division(self):
        resultado = self.calculadora.division(4, 2)
        self.assertEqual(resultado, 2)
    
    def test_potencia(self):
        resultado = self.calculadora.potencia(4, 2)
        self.assertEqual(resultado, 16)
    
    def test_raizcuadrada(self):
        resultado = self.calculadora.raizcuadrada(9)
        self.assertEqual(resultado, 3)
    
    

