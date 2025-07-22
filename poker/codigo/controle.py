import random
from jogador import Jogador

class Controle:
    def __init__(self):
        self.__valor_bb = 100
        self.__valor_sb = 50
        self.__bb = None
        self.__sb = None
        self.__start = 10000
        self.__jogadores = [Jogador(self.__start)]*9
        self.__player = random.randint(0,8)
        self.__aposta = self.__valor_bb
    def rodada(self):
        for i in range(9):
            if i == self.__player:
            else:
