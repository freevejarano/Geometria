from Circulo import Circulo
from Punto import Punto
from Figura import Figura
import math

a = Punto(0, 0)
b = Punto(0, 4)
c = [a, b]
circulo = Circulo(c)
#print("Mire",2* math.pi *  a.hallarDistancia(b))
#print(circulo.punto[0])
#p = circulo.hallarPerimetro()
z= Punto(5,5)


if(circulo.determinarEnElCirculo(z)):
    print("Holi")
else:
    print("Chao")


