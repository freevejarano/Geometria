from unittest import TestCase

from Circulo import Circulo
from Punto import Punto
from Figura import Figura

class Test(TestCase):
    def test_figuraCirculo(self):
        a=Punto(0,0)
        b=Punto(0,4)
        c=[a,b]
        circulo = Circulo(c)
      #  p= circulo.hallarPerimetro()
       # self.assertAlmostEqual(p, 25.13, places=1)
        a= circulo.hallarArea()
        self.assertAlmostEqual(a, 50.26, places=1)
        print(a)

