from abc import ABC, abstractmethod

class Transporte(ABC):

    def __init__(self, distancia, frete = 50.00):
        self.dist = distancia
        self.frete = frete

    @abstractmethod
    def calcular_frete(self):
        pass


class Moto(Transporte):
    fator = 0.50

    def __init__(self, distancia, frete):
        super().__init__(distancia, frete)

    def calcular_frete(self):
        valor = Moto.fator * self.dist * self.frete
        return f"{valor:.2f}"


class Caminhao(Transporte):
    fator = 1.2

    def __init__(self, distancia, frete):
        super().__init__(distancia, frete)

    def calcular_frete(self):
        if self.dist >= 50:
            valor = Caminhao.fator * self.dist * self.frete
            return f"{valor:.2f}"
        else:
            return "Frete não disponível. Distância mínima de 50km"



class Drone(Transporte):
    fator = 9.5

    def __init__(self, distancia, frete ):
        super().__init__(distancia, frete)

    def calcular_frete(self):
        if self.dist <= 10:
            valor = Drone.fator * self.dist * self.frete
            return f"{valor:.2f}"
        else:
            return "Frete não disponível. Distância máxima de 10km"

#print(__name__)