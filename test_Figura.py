from unittest import TestCase

from Circulo import Circulo
from Punto import Punto
from Figura import Figura
from Rectangulo import Rectangulo
from Triangulo import Triangulo


class Test(TestCase):
    def test_figuraCirculo(self):
        a=Punto(0,0)
        b=Punto(0,4)
        z=[a,b]
        circulo = Circulo(z)
        p= circulo.hallarPerimetro()
        self.assertAlmostEqual(p, 25.13, places=1)
        ar= circulo.hallarArea()
        self.assertAlmostEqual(ar, 50.26, places=1)

    def test_figuraTriangulo(self):
        a=Punto(0,0)
        b=Punto(2,0)
        c=Punto(0,2)
        z=[a,b,c]
        triangulo= Triangulo(z)
        p= triangulo.hallarPerimetro()
        self.assertAlmostEqual(p, 6.8, places=1)
        ar= triangulo.hallarArea()
        self.assertAlmostEqual(ar, 2, places=1)

    def test_figuraRectangulo(self):
        a=Punto(1,1)
        b=Punto(4,1)
        c=Punto(4,3)
        d=Punto(1,3)
        z=[a,b,c,d]
        rectangulo = Rectangulo(z)
        p = rectangulo.hallarPerimetro()
        self.assertAlmostEqual(p, 10, places=1)
        ar = rectangulo.hallarArea()
        self.assertAlmostEqual(ar, 6, places=1)


