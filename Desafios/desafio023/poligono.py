from abc import ABC, abstractmethod
import math

# definição da classe abstrata
class Poligono(ABC):
    def __init__(self, lados):
        self.qtd_lados = lados

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass

# definição das classes concretas
class Quadrado(Poligono):

    def __init__(self, lado = 1):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        return self.lado * self.qtd_lados

    def area(self):
        return self.lado * self.lado

class Circulo(Poligono):

    def __init__(self, raio = 1):
        super().__init__(0)
        self.lado = raio

    def perimetro(self):
        return 2 * math.pi * self.lado

    def area(self):
        return math.pi * self.lado ** 2




