import math

from Punto import Punto

#Clase Padre
from Punto import Punto

class Figura(object):
  #  def __init__(self,punto1=[]):
   #     punto = punto1
    #    print(punto1[1])

    def hallarPerimetro(self):
        n=len(self.punto)
        print(n)
        p=0
        if(n>2):
            for i in self.punto:
                if(i== n-1):
                    p+= self.punto[i].hallarDistancia(self.punto[0])
                    break
                else:
                    p+= self.punto[i].hallarDistancia(self.punto[i+1])
        elif(n==2):
            p= 2* math.pi * self.punto[0].hallarDistancia(self.punto[1])

        return p

    def areaCirculo(self):
        a=math.pi* math.pow(self.punto[0].hallarDistancia(self.punto[1]),2)
        return a

    def areaTriangulo(self):
        s= self.hallarPerimetro()/2
        a=math.sqrt(s*(s-self.punto[0].hallarDistancia(self.punto[1]))*(s-self.punto[1].hallarDistancia(self.punto[2]))* (s-self.punto[2].hallarDistancia(self.punto[0])))
        return a

    def areaRectangulo(self):
        a= self.punto[0].hallarDistancia(self.punto[1]) * self.punto[1].hallarDistancia(self.punto[2])
        return a

    def hallarArea(self):
        n = len(self.punto)
        a = 0

        switcher = {
            2: self.areaCirculo,
            3: self.areaTriangulo,
            4: self.areaRectangulo
        }
        a= switcher.get(self,lambda :"Figura invalida")
        return a






