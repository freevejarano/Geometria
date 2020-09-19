from Figura import Figura
class Circulo(Figura):
        pass

        def determinarEnElCirculo(self, p):
                centro = self.punto[0]
                radio = self.punto[1]
                return centro.hallarDistancia(p)<=centro.hallarDistancia(radio)






