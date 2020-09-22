from unittest import TestCase

from Punto import Punto
from Triangulo import Triangulo


class TestTriangulo(TestCase):
    def test_determinar_tipoEqui(self):
        a=Punto(0,0)
        b=Punto(4,0)
        c=Punto(2,3.47)
        equi= Triangulo([a,b,c])
        t= equi.determinarTipo()
        self.assertAlmostEqual(t, "equilatero")
        #print(t)

    def test_determinar_tipoIso(self):
        a=Punto(1,1)
        b=Punto(1,3)
        c=Punto(2,3)
        iso= Triangulo([a,b,c])
        t= iso.determinarTipo()
        self.assertAlmostEqual(t, "isoceles")
        #print(t)

    def test_determinar_tipoEsca(self):
        a=Punto(0,0)
        b=Punto(2,2)
        c=Punto(3,2)
        equi= Triangulo([a,b,c])
        t= equi.determinarTipo()
        self.assertAlmostEqual(t, "escaleno")
        #print(t)

