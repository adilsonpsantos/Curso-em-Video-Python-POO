from abc import ABC, abstractmethod


class BebidaQuente(ABC):

    def preparar(self):
        mensagem = "--- Iniciando o preparo ---\n"
        return mensagem

    def ferver_agua(self):
        mensagem = "--- 1. Fervendo a água a 100 graus Celsius. ---\n"
        return mensagem

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):

    def misturar(self):
        mensagem = "2. Passando água pressurizada pelo pó de café moído\n"
        return mensagem

    def servir(self):
        menagem = "3. Servindo em xícara pequena  \n"
        return menagem


class Cha(BebidaQuente):

    def misturar(self):
        mensagem = "2. Mergulhando o sachê de ervas na água\n"
        return mensagem

    def servir(self):
        menagem = "3. Servindo na caneca de porcelana com limão \n"
        return menagem


class Leite(BebidaQuente):

    def misturar(self):
        mensagem = "2. Misturando o café\n"
        return mensagem

    def servir(self):
        menagem = "3. Servindo \n"
        return menagem