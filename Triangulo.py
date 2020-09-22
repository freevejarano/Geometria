from Figura import Figura


class Triangulo(Figura):
    pass

    def determinarTipo(self):
        l1= self.punto[0].hallarDistancia(self.punto[1])
        l2= self.punto[1].hallarDistancia(self.punto[2])
        l3= self.punto[2].hallarDistancia(self.punto[0])

        l1= round(l1)
        l2= round(l2)
        l3= round(l3)
        #print(l1," ",l2," ",l3)
        tipo=""
        if (l1 == l2 and l2 == l3):
            tipo = "equilatero"
        elif (l1 == l2 or l1 == l3 or l2 == l3):
            tipo= "isoceles"
        else:
            tipo= "escaleno"

        return tipo;


