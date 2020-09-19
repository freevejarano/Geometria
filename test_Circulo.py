from unittest import TestCase

from Circulo import Circulo
from Punto import Punto


class Test(TestCase):
    def test_circulo(self):
        a = Punto(0, 0)
        b = Punto(0, 4)
        c = [a, b]
        circulo = Circulo(c)
        w = Punto(5, 5)
        z = Punto(2,2)
        self.assertTrue(circulo.determinarEnElCirculo(z),"Si")
        self.assertFalse(circulo.determinarEnElCirculo(w),"Si")
