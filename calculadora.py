from math import sqrt
class Calculadora:

    def suma(self, *args):
        value = 0
        for n in args:
            value += n
        return value
    
    def resta(self,a,b):
        return a - b
    
    def multiplicacion(self, *args):
        value = 1
        for n in args:
            value *= n
        return value

    def division(self,a,b):
        return a / b
    
    def potencia(self,a,b):
        return a**b
    
    def raizcuadrada(self, a):
        return sqrt(a)
