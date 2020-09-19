from unittest import TestCase

from Punto import Punto


class Test(TestCase):
    def test_punto(self):
       # a = Punto(1, 0)
       # b = Punto(-1, 0)
        a = Punto(0, 0)
        b = Punto(0, 4)
        dist = a.hallarDistancia(b)
        self.assertEqual(dist,2)
