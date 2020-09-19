from unittest import TestCase

from Circulo import Circulo
from Punto import Punto

a = Punto(0, 0)
b = Punto(0, 4)
c = [a, b]
circulo = Circulo(c)

class Test(TestCase):

    def test_EnElcirculoTrue(self):
        z = Punto(2,2)
        self.assertTrue(circulo.determinarEnElCirculo(z))

    def test_EnElCirculoFalse(self):
        w = Punto(5, 5)
        self.assertFalse(circulo.determinarEnElCirculo(w))
