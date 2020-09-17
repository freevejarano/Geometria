from unittest import TestCase

from Circulo import Circulo
from Punto import Punto
from Figura import Figura

class Test(TestCase):
    def test_figura(self):
        a=Punto(0,0)
        b=Punto(0,4)
        circulo = Circulo([a,b])
        p= circulo.hallarPerimetro()
        print(p)
        #self.assertEqual(p,50.26)
